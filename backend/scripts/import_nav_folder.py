"""把本地文件夹里的书签/快捷方式导入导航板块。

用法 (在 backend 目录下):
  .venv/Scripts/python scripts/import_nav_folder.py <文件夹或书签HTML路径>

规则:
- 传文件夹: 一级子文件夹 → 分类; 分类下的 .url/.desktop/.txt/.html 文件 → 导航链接
- 传 .html 文件: 按 Chrome/Firefox 导出的书签格式解析（H3 文件夹 → 分类）
- 输出: backend/app/seed_nav.json，重启后端后生效，服务器部署时随镜像带上
"""

from __future__ import annotations

import json
import re
import sys
import uuid
from pathlib import Path
from urllib.parse import urlparse

SEED_FILE = Path(__file__).resolve().parents[1] / "app" / "seed_nav.json"

URL_RE = re.compile(r"https?://[^\s\"'<>]+")
DOMAIN_RE = re.compile(r"^(?:[a-z0-9-]+\.)+[a-z]{2,}(?:/\S*)?$", re.I)


def _id() -> str:
    return uuid.uuid4().hex[:8]


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
            name = re.sub(r"<[^>]+>", "", m.group(1)).strip() or "未命名分类"
            stack.append(name)
            cats.setdefault(stack[-1], [])
        elif m.group(2) is not None:
            url = m.group(2).strip()
            name = re.sub(r"<[^>]+>", "", m.group(3) or "").strip() or urlparse(url).netloc
            if url.startswith(("http://", "https://")):
                cats.setdefault(stack[-1], []).append((name, url))
        elif len(stack) > 1:
            stack.pop()
    return {k: v for k, v in cats.items() if v}


def from_directory(root: Path) -> tuple[dict[str, list[tuple[str, str]]], list[str]]:
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
        elif suffix in (".url", ".desktop", ".txt", ".lnk"):
            parsed = parse_url_file(p) if suffix != ".lnk" else None
            if parsed:
                cats.setdefault(cat_name, []).append(parsed)
            else:
                skipped.append(str(rel))
        else:
            skipped.append(str(rel))
    return cats, skipped


def build_seed(groups: dict[str, list[tuple[str, str]]]) -> dict:
    categories = []
    for name, links in groups.items():
        seen: set[str] = set()
        items = []
        for link_name, url in links:
            if url in seen:
                continue
            seen.add(url)
            items.append({"id": _id(), "name": link_name[:50], "url": url})
        if items:
            categories.append({"id": _id(), "name": name[:30], "links": items})
    return {"categories": categories}


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    target = Path(sys.argv[1])
    if not target.exists():
        print(f"路径不存在: {target}")
        sys.exit(1)

    if target.is_file():
        groups = parse_html_bookmarks(target)
        skipped: list[str] = []
    else:
        groups, skipped = from_directory(target)

    if not groups:
        print("没有提取到任何链接（支持 .url/.desktop/.txt/书签.html）")
        sys.exit(1)

    seed = build_seed(groups)
    SEED_FILE.write_text(
        json.dumps(seed, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    total = sum(len(c["links"]) for c in seed["categories"])
    print(f"✅ 已写入 {SEED_FILE}")
    print(f"   {len(seed['categories'])} 个分类，共 {total} 条导航:")
    for c in seed["categories"]:
        print(f"   - {c['name']}: {len(c['links'])} 条")
    if skipped:
        print(f"   跳过 {len(skipped)} 个无法识别的文件: {', '.join(skipped[:8])}")
    print("重启后端后生效；服务器上重新执行 deploy.sh 即可带上。")


if __name__ == "__main__":
    main()
