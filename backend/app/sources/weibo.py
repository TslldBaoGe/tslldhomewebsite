"""Weibo hot search.

The ajax endpoint rejects cookieless clients, so we first visit the homepage
with a real-browser UA to collect cookies, then call the API with them.
"""

from __future__ import annotations

from urllib.parse import quote

import httpx

from ..net import with_retry

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
)

HOME_URL = "https://weibo.com/"
API_URL = "https://weibo.com/ajax/side/hotSearch"


def _headers(extra: dict | None = None) -> dict:
    h = {
        "User-Agent": UA,
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Referer": "https://weibo.com/",
    }
    if extra:
        h.update(extra)
    return h


async def _fetch_items(client: httpx.AsyncClient) -> list[dict]:
    await with_retry(lambda: client.get(HOME_URL, headers=_headers()))
    resp = await with_retry(
        lambda: client.get(API_URL, headers=_headers({"Accept": "application/json"}))
    )
    resp.raise_for_status()
    payload = resp.json()
    if payload.get("ok") != 1:
        raise RuntimeError(f"weibo api returned ok={payload.get('ok')!r}")

    items = []
    for entry in payload.get("data", {}).get("realtime", []):
        word = (entry.get("word") or "").strip()
        if not word:
            continue
        scheme = entry.get("word_scheme") or word
        items.append(
            {
                "title": word,
                "hot": entry.get("num") or 0,
                "tag": (entry.get("label_name") or "").strip(),
                "url": "https://s.weibo.com/weibo?q=" + quote(scheme),
            }
        )
    return items


async def fetch_weibo_hot(client: httpx.AsyncClient, fetched_at: str) -> dict:
    try:
        items = await _fetch_items(client)
    except (httpx.HTTPStatusError, RuntimeError):
        # cookies may have expired - drop them and bootstrap once more
        client.cookies.clear()
        items = await _fetch_items(client)

    return {
        "platform": "weibo",
        "name": "微博热搜",
        "fetched_at": fetched_at,
        "items": items,
    }
