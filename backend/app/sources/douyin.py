"""Douyin (抖音) hot search via the iesdouyin billboard API."""

from urllib.parse import quote

import httpx

from ..net import with_retry

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
)

API_URL = "https://www.iesdouyin.com/web/api/v2/hotsearch/billboard/word/"

# 1=热, 2=新, 3=爆; 0 means no tag
LABEL_MAP = {1: "热", 2: "新", 3: "爆"}


async def fetch_douyin_hot(client: httpx.AsyncClient, fetched_at: str) -> dict:
    resp = await with_retry(
        lambda: client.get(
            API_URL,
            headers={
                "User-Agent": UA,
                "Accept": "application/json",
                "Referer": "https://www.douyin.com/",
            },
        )
    )
    resp.raise_for_status()
    payload = resp.json()
    if payload.get("status_code") != 0:
        raise RuntimeError(f"douyin api returned status_code={payload.get('status_code')!r}")

    items = []
    for entry in payload.get("word_list", []):
        word = (entry.get("word") or "").strip()
        if not word:
            continue
        items.append(
            {
                "title": word,
                "hot": entry.get("hot_value") or 0,
                "tag": LABEL_MAP.get(entry.get("label"), ""),
                "url": "https://www.douyin.com/search/" + quote(word),
            }
        )

    return {
        "platform": "douyin",
        "name": "抖音热搜",
        "fetched_at": fetched_at,
        "items": items,
    }
