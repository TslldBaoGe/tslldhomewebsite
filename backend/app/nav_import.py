"""把本地文件夹/书签 HTML 解析成导航板块的分类结构。

供 /api/nav/import 接口和 scripts/import_nav_folder.py 脚本共用。
"""

from __future__ import annotations

import re
from urllib.parse import urlparse

URL_RE = re.compile(r"https?://[^\s\"'<>]+")
DOMAIN_RE = re.compile(r"^(?:[a-z0-9-]+\.)+[a-z]{2,}(?:/\S*)?$", re.I)


def _strip_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text or "").strip()


def extract_url(text: str) -> str | None:
    m = URL_RE.search(text)
    if m:
        return m.group(0).rstrip("\\")
    for line in text.splitlines():
        line = line.strip()
        if line and DOMAIN_RE.match(line):
            return "https://" + line
    return None


def parse_url_file(path: Path) -> tuple[str, str] | None:
    """.url / .desktop / .txt 文件里提取第一条链接，文件名作为默认名称。"""
    url = extract_url(path.read_text(encoding="utf-8", errors="ignore"))
    return (path.stem, url) if url else None


def parse_html_bookmarks(path: Path) -> dict[str, list[tuple[str, str]]]:
    """Chrome/Firefox 书签导出: <H3>分类</H3> ... <A HREF="...">名称</A>"""
    html = path.read_text(encoding="utf-8", errors="ignore")
    cats: dict[str, list[tuple[str, str]]] = {}
    stack = ["导入书签"]
    for m in re.finditer(
        r"<H3[^>]*>(.*?)</H3>|<A\s[^>]*HREF=\"([^\"]+)\"[^>]*>(.*?)</A>|</DL>",
        html,
        re.I | re.S,
    ):
        if m.group(1) is not None:
            name = _strip_tags(m.group(1)) or "未命名分类"
            stack.append(name)
            cats.setdefault(stack[-1], [])
        elif m.group(2) is not None:
            url = m.group(2).strip()
            name = _strip_tags(m.group(3) or "") or urlparse(url).netloc
            if url.startswith(("http://", "https://")):
                cats.setdefault(stack[-1], []).append((name, url))
        elif len(stack) > 1:
            stack.pop()
    return {k: v for k, v in cats.items() if v}


def from_directory(root: Path) -> tuple[dict[str, list[tuple[str, str]]], list[str]]:
    """遍历目录：一级子文件夹为分类，更深层以「父/子」命名，根文件归入未分类。"""
    cats: dict[str, list[tuple[str, str]]] = {}
    skipped: list[str] = []
    for p in sorted(root.rglob("*")):
        if p.is_dir():
            continue
        rel = p.relative_to(root)
        parts = rel.parts
        cat_name = "未分类" if len(parts) == 1 else "/".join(parts[:-1])
        suffix = p.suffix.lower()
        if suffix in (".html", ".htm"):
            for sub_name, links in parse_html_bookmarks(p).items():
                full = cat_name if cat_name == "未分类" else f"{cat_name} · {sub_name}"
                cats.setdefault(full, []).extend(links)
        elif suffix in (".url", ".desktop", ".txt"):
            parsed = parse_url_file(p)
            if parsed:
                cats.setdefault(cat_name, []).append(parsed)
            else:
                skipped.append(str(rel))
        else:
            skipped.append(str(rel))
    return cats, skipped


def build_categories(groups: dict[str, list[tuple[str, str]]]) -> list[dict]:
    """去重合并为 [{name, links: [{name, url}]}] 结构（不带 id，入库时再分配）。"""
    categories = []
    for name, links in groups.items():
        seen: set[str] = set()
        items = []
        for link_name, url in links:
            if url in seen:
                continue
            seen.add(url)
            items.append({"name": link_name[:50], "url": url})
        if items:
            categories.append({"name": name[:30], "links": items})
    return categories
