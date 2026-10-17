import asyncio
import hmac
import logging
import os
from contextlib import asynccontextmanager
from datetime import datetime, timezone, timedelta
from pathlib import Path

import httpx
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .cache import TTLCache
from . import nav_import
from .sources import bilibili, codefather, douyin, weibo, zhihu
from .store import (
    NavStore,
    add_category,
    add_link,
    delete_category,
    delete_link,
    merge_import,
    rename_category,
    update_link,
)
from .grammar import load_grammar, find_item

logger = logging.getLogger("uvicorn.error")

CACHE_TTL_SECONDS = int(os.environ.get("CACHE_TTL_SECONDS", "300"))
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "changeme")
if ADMIN_PASSWORD == "changeme":
    logger.warning(
        "ADMIN_PASSWORD is still the default 'changeme' - "
        "set a real one via the ADMIN_PASSWORD env before exposing publicly!"
    )

DATA_DIR = Path(os.environ.get("DATA_DIR") or Path(__file__).resolve().parents[2] / "data")
nav_store = NavStore(DATA_DIR / "nav.json")

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
        trust_env=False,  # 上游都是国内站点，无视系统代理/环境代理直连
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


@app.get("/api/nav")
async def nav_data():
    return await nav_store.get()


# ---- 导航板块管理（需管理密码） ----

class CategoryIn(BaseModel):
    name: str


class LinkIn(BaseModel):
    name: str
    url: str


class LinkMoveIn(BaseModel):
    category_id: str
    name: str
    url: str


class PasswordIn(BaseModel):
    password: str


def require_admin(x_admin_token: str = Header(default="")):
    if not x_admin_token or not hmac.compare_digest(x_admin_token, ADMIN_PASSWORD):
        raise HTTPException(status_code=401, detail="管理密码错误")


@app.post("/api/nav/auth")
async def nav_auth(body: PasswordIn):
    if not hmac.compare_digest(body.password, ADMIN_PASSWORD):
        raise HTTPException(status_code=401, detail="管理密码错误")
    return {"ok": True}


@app.post("/api/nav/category", dependencies=[Depends(require_admin)])
async def nav_add_category(body: CategoryIn):
    try:
        return await nav_store.mutate(lambda d: add_category(d, body.name))
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.put("/api/nav/category/{cid}", dependencies=[Depends(require_admin)])
async def nav_rename_category(cid: str, body: CategoryIn):
    try:
        return await nav_store.mutate(lambda d: rename_category(d, cid, body.name))
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.delete("/api/nav/category/{cid}", dependencies=[Depends(require_admin)])
async def nav_delete_category(cid: str):
    try:
        return await nav_store.mutate(lambda d: delete_category(d, cid))
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@app.post("/api/nav/link", dependencies=[Depends(require_admin)])
async def nav_add_link(body: LinkMoveIn):
    try:
        return await nav_store.mutate(lambda d: add_link(d, body.category_id, body.name, body.url))
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.put("/api/nav/link/{lid}", dependencies=[Depends(require_admin)])
async def nav_update_link(lid: str, body: LinkIn):
    try:
        return await nav_store.mutate(lambda d: update_link(d, lid, body.name, body.url))
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.delete("/api/nav/link/{lid}", dependencies=[Depends(require_admin)])
async def nav_delete_link(lid: str):
    try:
        return await nav_store.mutate(lambda d: delete_link(d, lid))
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


# ---------------- 英语语法板块（只读，不影响其他板块） ----------------

_GRAMMAR = load_grammar()


@app.get("/api/grammar")
async def grammar():
    return _GRAMMAR


@app.get("/api/grammar/{item_id}")
async def grammar_item(item_id: str):
    cat, item = find_item(_GRAMMAR, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail=f"语法点不存在：{item_id}")
    return {"category": cat["name"], "item": item}


class ImportIn(BaseModel):
    path: str
    mode: str = "merge"  # merge=按分类合并去重, replace=覆盖全部


@app.post("/api/nav/import", dependencies=[Depends(require_admin)])
async def nav_import_folder(body: ImportIn):
    """读取服务器本地文件夹/书签 HTML 并导入导航板块。"""
    path = Path(body.path.strip().strip('"'))
    if body.mode not in ("merge", "replace"):
        raise HTTPException(status_code=400, detail="mode 只能是 merge 或 replace")
    if not path.exists():
        raise HTTPException(status_code=400, detail=f"路径不存在：{path}")
    try:
        if path.is_file():
            groups = nav_import.parse_html_bookmarks(path)
            skipped: list[str] = []
        else:
            groups, skipped = nav_import.from_directory(path)
    except OSError as exc:
        raise HTTPException(status_code=400, detail=f"读取失败：{exc}") from exc

    categories = nav_import.build_categories(groups)
    if not categories:
        raise HTTPException(
            status_code=400,
            detail="没有提取到任何链接（支持 .url/.desktop/.txt 及书签导出的 .html）",
        )

    data = await nav_store.mutate(lambda d: merge_import(d, categories, body.mode))
    return {
        "data": data,
        "imported": {
            "categories": len(categories),
            "links": sum(len(c["links"]) for c in categories),
        },
        "skipped": skipped[:8],
    }


# Production mode: serve the built frontend from the same port as the API.
# Mounted last so /api/* routes keep taking precedence.
_FRONTEND_DIST = Path(
    os.environ.get("FRONTEND_DIST")
    or Path(__file__).resolve().parents[2] / "frontend" / "dist"
)
if _FRONTEND_DIST.is_dir():
    app.mount("/", StaticFiles(directory=_FRONTEND_DIST, html=True), name="frontend")
    logger.info("serving frontend from %s", _FRONTEND_DIST)
