"""央视新闻数据源。

数据来自 CNTV 公开栏目接口：
1) getVideoListByColumn 取新闻联播最近几期节目（guid 列表）
2) videoinfoByGuid 取每期 brief（本期节目主要内容），按行拆出分条新闻

每条新闻：标题、期次日期 tag、该期联播视频页链接、发布时间戳。
"""

import re

import httpx

COLUMN_ID = "TOPC1451528971114112"  # 新闻联播
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    ),
    "Referer": "https://tv.cctv.com/",
}
EPISODES = 3  # 取最近几期联播

MAIN_RE = re.compile(r"^\d+[.、]\s*(.+?)[；;。]?\s*$")
SUB_RE = re.compile(r"^[（(]\d+[)）]\s*(.+?)[；;。]?\s*$")


async def _fetch_episode(client: httpx.AsyncClient, guid: str) -> dict:
    r = await client.get(
        f"https://api.cntv.cn/video/videoinfoByGuid?guid={guid}&serviceId=tvcctv",
        headers=HEADERS,
    )
    r.raise_for_status()
    return r.json()


def _parse_brief(brief: str) -> list[str]:
    """从「本期节目主要内容」解析分条新闻标题。"""
    titles = []
    for line in brief.splitlines():
        line = line.strip()
        if not line or "本期节目主要内容" in line or line.startswith("（《"):
            continue
        m = MAIN_RE.match(line) or SUB_RE.match(line)
        if m:
            t = m.group(1).strip()
            if len(t) >= 5:
                titles.append(t)
    return titles


def _episode_tag(title: str) -> str:
    """《新闻联播》 20261017 19:00 → 联播 10-17"""
    m = re.search(r"(\d{4})(\d{2})(\d{2})", title)
    return f"联播 {m.group(2)}-{m.group(3)}" if m else "联播"


async def fetch_cctv_news(client: httpx.Client, fetched_at: str) -> dict:
    r = await client.get(
        f"https://api.cntv.cn/NewVideo/getVideoListByColumn?id={COLUMN_ID}"
        f"&n={EPISODES}&sort=desc&p=1&mode=0&serviceId=tvcctv",
        headers=HEADERS,
    )
    r.raise_for_status()
    episodes = (r.json().get("data") or {}).get("list") or []

    items, seen = [], set()
    for ep in episodes:
        guid = ep.get("guid")
        page_url = ep.get("url") or ""
        tag = _episode_tag(ep.get("title") or "")
        try:
            info = await _fetch_episode(client, guid)
        except (httpx.HTTPError, ValueError):
            continue
        ts = ep.get("time") or ""
        for t in _parse_brief(info.get("brief") or ""):
            if t in seen:
                continue
            seen.add(t)
            items.append(
                {
                    "title": t,
                    "hot": 0,
                    "tag": tag,
                    "url": page_url,
                    "time": ts,
                }
            )
        if len(items) >= 60:
            break

    if not items:
        raise RuntimeError("cctv 新闻解析为空（接口可能变更）")

    return {
        "platform": "cctv",
        "name": "央视新闻",
        "fetched_at": fetched_at,
        "items": items[:60],
    }
