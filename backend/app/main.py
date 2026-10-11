import asyncio
import logging
import os
from contextlib import asynccontextmanager
from datetime import datetime, timezone, timedelta
from pathlib import Path

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .cache import TTLCache
from .sources import bilibili, codefather, douyin, weibo, zhihu

logger = logging.getLogger("uvicorn.error")

CACHE_TTL_SECONDS = int(os.environ.get("CACHE_TTL_SECONDS", "300"))

CST = timezone(timedelta(hours=8))  # site audience is CN, keep timestamps on +08:00

SOURCES = {
    "weibo": weibo.fetch_weibo_hot,
    "douyin": douyin.fetch_douyin_hot,
    "zhihu": zhihu.fetch_zhihu_hot,
    "bilibili": bilibili.fetch_bilibili_hot,
    "codefather": codefather.fetch_codefather_news,
}


def _now_cst() -> str:
    return datetime.now(CST).isoformat(timespec="seconds")


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.http = httpx.AsyncClient(
        timeout=httpx.Timeout(15.0),
        follow_redirects=True,
    )
    app.state.cache = TTLCache(CACHE_TTL_SECONDS)
    yield
    await app.state.http.aclose()


app = FastAPI(title="tsll Website API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:4173",
        "http://127.0.0.1:4173",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)


async def _get_hotlist(
    client: httpx.AsyncClient, cache: TTLCache, platform: str, refresh: bool = False
) -> dict:
    async def fetch():
        return await SOURCES[platform](client, _now_cst())

    try:
        if refresh:
            payload = await fetch()
            await cache.put(platform, payload)
            return payload
        return await cache.get_or_set(platform, fetch)
    except Exception as exc:
        logger.warning("fetching %s hotlist failed: %s", platform, exc)
        raise HTTPException(status_code=502, detail=f"获取{platform}热搜失败：{exc}") from exc


@app.get("/api/health")
async def health():
    return {"status": "ok", "time": _now_cst()}


@app.get("/api/news/{platform}")
async def hotlist(platform: str, refresh: bool = False):
    if platform not in SOURCES:
        raise HTTPException(status_code=404, detail=f"未知平台：{platform}，可用：{list(SOURCES)}")
    return await _get_hotlist(app.state.http, app.state.cache, platform, refresh)


@app.get("/api/news")
async def all_hotlists(refresh: bool = False):
    """All platforms at once; a failing platform is reported in `errors`
    instead of failing the whole response."""

    async def load(platform: str):
        try:
            return platform, await _get_hotlist(
                app.state.http, app.state.cache, platform, refresh
            )
        except HTTPException:
            return platform, None

    results = await asyncio.gather(*(load(p) for p in SOURCES))
    data = {platform: payload for platform, payload in results}
    errors = {p: "抓取失败，请稍后重试" for p, payload in data.items() if payload is None}
    return {"updated_at": _now_cst(), "data": data, "errors": errors}


# Production mode: serve the built frontend from the same port as the API.
# Mounted last so /api/* routes keep taking precedence.
_FRONTEND_DIST = Path(
    os.environ.get("FRONTEND_DIST")
    or Path(__file__).resolve().parents[2] / "frontend" / "dist"
)
if _FRONTEND_DIST.is_dir():
    app.mount("/", StaticFiles(directory=_FRONTEND_DIST, html=True), name="frontend")
    logger.info("serving frontend from %s", _FRONTEND_DIST)
