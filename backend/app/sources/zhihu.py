"""Zhihu hot list via the mobile app API (works without auth)."""

from __future__ import annotations

import re

import httpx

from ..net import with_retry

UA = (
    "osee2unifiedRelease/2245 osee2unifiedReleaseVersion/10.36.0 "
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15"
)

API_URL = "https://api.zhihu.com/topstory/hot-list?limit=50"

# card_label.type -> badge text
LABEL_MAP = {"boiling": "沸", "hot": "热", "new": "新"}

_HEAT_RE = re.compile(r"([\d.]+)\s*万")


def _parse_heat(detail_text: str) -> int:
    """detail_text looks like '2590 万热度'."""
    match = _HEAT_RE.search(detail_text or "")
    if not match:
        return 0
    try:
        return int(float(match.group(1)) * 10000)
    except ValueError:
        return 0


async def fetch_zhihu_hot(client: httpx.AsyncClient, fetched_at: str) -> dict:
    resp = await with_retry(
        lambda: client.get(
            API_URL,
            headers={"User-Agent": UA, "Accept": "application/json"},
        )
    )
    resp.raise_for_status()
    payload = resp.json()
    if not isinstance(payload.get("data"), list):
        raise RuntimeError(f"zhihu api unexpected payload: {str(payload)[:120]}")

    items = []
    for entry in payload["data"]:
        target = entry.get("target") or {}
        title = (target.get("title") or "").strip()
        if not title:
            continue
        question_id = target.get("id")
        url = (
            f"https://www.zhihu.com/question/{question_id}"
            if question_id
            else "https://www.zhihu.com/hot"
        )
        label_type = (entry.get("card_label") or {}).get("type") or ""
        items.append(
            {
                "title": title,
                "hot": _parse_heat(entry.get("detail_text") or ""),
                "tag": LABEL_MAP.get(label_type, ""),
                "url": url,
            }
        )

    return {
        "platform": "zhihu",
        "name": "知乎热榜",
        "fetched_at": fetched_at,
        "items": items,
    }
