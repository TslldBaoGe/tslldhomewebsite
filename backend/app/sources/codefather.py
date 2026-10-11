"""Codefather (鱼皮AI导航) AI news feed.

The site is a Next.js app with no public list API - the feed is
server-rendered into the page's RSC flight payload, so we fetch the page
HTML and pull items out with targeted regexes against that payload.
"""

from __future__ import annotations

import re

import httpx

from ..net import with_retry

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
)

PAGE_URL = "https://ai.codefather.cn/news"
MAX_ITEMS = 30

# RSC payload markers, e.g. [\"div\",\"2108948704403685387\",{...}
_ITEM_RE = re.compile(re.escape(r'\"div\",\"') + r"(\d{15,25})" + re.escape(r'\"'))
_TITLE_RE = re.compile(
    re.escape(r'text-slate-900\",\"children\":\"') + r"(.+?)" + re.escape(r'\"')
)
_SUMMARY_RE = re.compile(
    re.escape(r'text-slate-600\",\"children\":\"') + r"(.+?)" + re.escape(r'\"')
)
_HREF_RE = re.compile(re.escape(r'\"href\":\"') + r"(/news/\d+)")


def _unescape(text: str) -> str:
    return text.replace(r"\"", '"').replace(r"\n", " ").strip()


async def fetch_codefather_news(client: httpx.AsyncClient, fetched_at: str) -> dict:
    resp = await with_retry(
        lambda: client.get(
            PAGE_URL,
            headers={"User-Agent": UA, "Accept": "text/html"},
        )
    )
    resp.raise_for_status()
    html = resp.text

    matches = list(_ITEM_RE.finditer(html))
    items = []
    seen = set()
    for idx, match in enumerate(matches):
        news_id = match.group(1)
        if news_id in seen:
            continue
        seen.add(news_id)

        # each item lives between its marker and the next one
        end = matches[idx + 1].start() if idx + 1 < len(matches) else match.start() + 6000
        chunk = html[match.start() : end]

        title_m = _TITLE_RE.search(chunk)
        if not title_m:
            continue
        summary_m = _SUMMARY_RE.search(chunk)
        href_m = _HREF_RE.search(chunk)

        items.append(
            {
                "title": _unescape(title_m.group(1)),
                "hot": 0,
                "tag": "",
                "url": "https://ai.codefather.cn"
                + (href_m.group(1) if href_m else f"/news/{news_id}"),
                "summary": _unescape(summary_m.group(1)) if summary_m else "",
            }
        )
        if len(items) >= MAX_ITEMS:
            break

    if not items:
        raise RuntimeError("codefather page rendered no news (layout may have changed)")

    return {
        "platform": "codefather",
        "name": "AI资讯",
        "fetched_at": fetched_at,
        "items": items,
    }
