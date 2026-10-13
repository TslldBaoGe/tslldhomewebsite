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


SENSITIVE_RE = re.compile(r"密码|账号|password|account|secret", re.I)
MAX_TEXT_FILE_BYTES = 256 * 1024


def _link_name_from_text(text: str, fallback: str) -> str:
    """`1` 收藏文件格式：第一行是说明（可无），随后是网址。"""
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if URL_RE.match(line) or DOMAIN_RE.match(line):
            continue
        return line[:50]
    return fallback


def _pretty_item(item: str) -> str:
    """目录名「内容」部分：优先取括号里的中文名，如 www.zhihu.com（知乎）→ 知乎。"""
    m = re.search(r"（(.+?)）", item)
    if m:
        return m.group(1).strip() or item
    return item.strip()


def from_directory(root: Path) -> tuple[dict[str, list[tuple[str, str]]], list[str]]:
    """遍历目录并按「分类-内容」约定解析。

    - 一级目录名 `X-Y`：X 为分类（允许数字序号前缀如 `1-AI`），Y 为内容
    - `1` 等无扩展名小文本文件：首行说明 + 网址，是该目录的收藏链接
    - 目录内容为空但 Y 本身是域名（如 office安装-www.officetool.plus）时直接生成链接
    - 根目录下 .url/.txt 等文件：文件名 `-` 前为分类（纯数字前缀视为日期序号，忽略）
    - 含密码/账号字样的文件、二进制和软件文件一律跳过
    """
    cats: dict[str, list[tuple[str, str]]] = {}
    skipped: list[str] = []

    def add(cat: str, name: str, url: str) -> None:
        url = url.strip()
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        cats.setdefault(cat, []).append((name or url, url))

    for top in sorted(root.iterdir()):
        if SENSITIVE_RE.search(top.name):
            skipped.append(f"{top.name}/（敏感信息，跳过）")
            continue

        if top.is_file():
            suffix = top.suffix.lower()
            if suffix not in (".url", ".txt", ".desktop"):
                skipped.append(top.name)
                continue
            parsed = parse_url_file(top)
            if not parsed:
                skipped.append(top.name)
                continue
            cat, stem = "未分类", parsed[0]
            if "-" in stem:
                prefix, rest = stem.split("-", 1)
                if prefix.isdigit():
                    cat, stem = "未分类", rest  # 纯数字前缀视为日期，不作为分类
                else:
                    cat, stem = prefix.strip(), rest
            add(cat, stem, parsed[1])
            continue

        # 目录：解析「分类-内容」
        if "-" in top.name:
            prefix, item = top.name.split("-", 1)
            cat = re.sub(r"^\d+", "", prefix).strip() or prefix.strip()
            item = item.strip()
        else:
            cat, item = top.name, ""

        links: list[tuple[str, str]] = []
        for p in sorted(top.rglob("*")):
            if p.is_dir() or SENSITIVE_RE.search(p.name):
                continue
            rel = str(p.relative_to(root))
            suffix = p.suffix.lower()
            if suffix in (".url", ".txt", ".desktop"):
                parsed = parse_url_file(p)
                if parsed:
                    links.append(parsed)
                else:
                    skipped.append(rel)
            elif suffix == "" and p.stat().st_size <= MAX_TEXT_FILE_BYTES:
                text = p.read_text(encoding="utf-8", errors="ignore")
                url = extract_url(text)
                if url:
                    links.append((_pretty_item(item), url))
                else:
                    skipped.append(rel)
            else:
                skipped.append(rel)

        # 目录里没有链接，但「内容」本身是域名（office安装-www.officetool.plus）
        if not links and item and DOMAIN_RE.match(item):
            links.append((_pretty_item(item), "https://" + item.split("（")[0]))

        if links:
            cats.setdefault(cat, []).extend(links)

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
