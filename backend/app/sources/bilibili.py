"""Bilibili hot search via the web search square API."""

from __future__ import annotations

import re
from urllib.parse import quote

import httpx

from ..net import with_retry

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
)

API_URL = "https://api.bilibili.com/x/web-interface/search/square?limit=50"

_TAG_RE = re.compile(r"<[^>]+>")


def _clean(text: str) -> str:
    return _TAG_RE.sub("", text or "").strip()


async def fetch_bilibili_hot(client: httpx.AsyncClient, fetched_at: str) -> dict:
    resp = await with_retry(
        lambda: client.get(
            API_URL,
            headers={
                "User-Agent": UA,
                "Accept": "application/json",
                "Referer": "https://www.bilibili.com/",
            },
        )
    )
    resp.raise_for_status()
    payload = resp.json()
    if payload.get("code") != 0:
        raise RuntimeError(
            f"bilibili api code={payload.get('code')} msg={payload.get('message')}"
        )

    trending = (payload.get("data") or {}).get("trending") or {}
    items = []
    for entry in trending.get("list") or []:
        keyword = (entry.get("keyword") or "").strip()
        if not keyword:
            continue
        # show_name sometimes carries markup; keyword is always plain text
        display = _clean(entry.get("show_name")) or keyword
        items.append(
            {
                "title": display,
                "hot": entry.get("heat_score") or 0,
                "tag": "",
                "url": "https://search.bilibili.com/all?keyword=" + quote(keyword),
            }
        )

    return {
        "platform": "bilibili",
        "name": "B站热搜",
        "fetched_at": fetched_at,
        "items": items,
    }
