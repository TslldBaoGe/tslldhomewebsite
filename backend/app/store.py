"""Navigation bookmarks store - JSON file persistence with in-memory cache.

The nav data survives container rebuilds via the data volume (DATA_DIR).
First run seeds from backend/app/seed_nav.json when present (shipped via
git), otherwise from a small built-in example.
"""

from __future__ import annotations

import asyncio
import json
import os
import uuid
from pathlib import Path

SEED_FILE = Path(__file__).resolve().parent / "seed_nav.json"


def _new_id() -> str:
    return uuid.uuid4().hex[:8]


def normalize_url(url: str) -> str:
    url = (url or "").strip()
    if url and not url.lower().startswith(("http://", "https://")):
        url = "https://" + url
    return url


def _builtin_seed() -> dict:
    return {
        "categories": [
            {
                "id": _new_id(),
                "name": "常用工具",
                "links": [
                    {"id": _new_id(), "name": "GitHub", "url": "https://github.com"},
                    {"id": _new_id(), "name": "哔哩哔哩", "url": "https://www.bilibili.com"},
                ],
            },
            {
                "id": _new_id(),
                "name": "学习资源",
                "links": [
                    {"id": _new_id(), "name": "MDN Web 文档", "url": "https://developer.mozilla.org/zh-CN/"},
                ],
            },
        ]
    }


def _load_seed() -> dict:
    if SEED_FILE.exists():
        try:
            data = json.loads(SEED_FILE.read_text(encoding="utf-8"))
            if isinstance(data.get("categories"), list):
                return data
        except (json.JSONDecodeError, OSError):
            pass
    return _builtin_seed()


class NavStore:
    def __init__(self, path: Path):
        self.path = path
        self._lock = asyncio.Lock()
        self._data: dict | None = None

    def _load_sync(self) -> dict:
        if self.path.exists():
            try:
                data = json.loads(self.path.read_text(encoding="utf-8"))
                if isinstance(data.get("categories"), list):
                    return data
            except (json.JSONDecodeError, OSError):
                pass
        return _load_seed()

    def _save_sync(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(
            json.dumps(self._data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        os.replace(tmp, self.path)

    async def get(self) -> dict:
        async with self._lock:
            if self._data is None:
                self._data = self._load_sync()
                self._save_sync()
            return self._data

    async def mutate(self, fn):
        """Run fn(data) under the lock, persist, and return the updated data.

        fn mutates the dict in place and may raise KeyError/ValueError.
        """
        async with self._lock:
            if self._data is None:
                self._data = self._load_sync()
            fn(self._data)
            self._save_sync()
            return self._data


def _get_category(data: dict, cid: str) -> dict:
    for cat in data["categories"]:
        if cat["id"] == cid:
            return cat
    raise KeyError(f"分类不存在: {cid}")


def _get_link(data: dict, lid: str) -> tuple[dict, dict]:
    for cat in data["categories"]:
        for link in cat["links"]:
            if link["id"] == lid:
                return cat, link
    raise KeyError(f"导航不存在: {lid}")


def add_category(data: dict, name: str) -> dict:
    name = (name or "").strip()
    if not name:
        raise ValueError("分类名不能为空")
    cat = {"id": _new_id(), "name": name, "links": []}
    data["categories"].append(cat)
    return cat


def rename_category(data: dict, cid: str, name: str) -> dict:
    name = (name or "").strip()
    if not name:
        raise ValueError("分类名不能为空")
    _get_category(data, cid)["name"] = name
    return _get_category(data, cid)


def delete_category(data: dict, cid: str) -> None:
    cat = _get_category(data, cid)
    data["categories"].remove(cat)


def add_link(data: dict, cid: str, name: str, url: str) -> dict:
    name = (name or "").strip()
    url = normalize_url(url)
    if not name or not url:
        raise ValueError("名称和网址不能为空")
    link = {"id": _new_id(), "name": name, "url": url}
    _get_category(data, cid)["links"].append(link)
    return link


def update_link(data: dict, lid: str, name: str, url: str) -> dict:
    name = (name or "").strip()
    url = normalize_url(url)
    if not name or not url:
        raise ValueError("名称和网址不能为空")
    _, link = _get_link(data, lid)
    link["name"] = name
    link["url"] = url
    return link


def delete_link(data: dict, lid: str) -> None:
    cat, link = _get_link(data, lid)
    cat["links"].remove(link)


def merge_import(data: dict, categories: list[dict], mode: str = "merge") -> dict:
    """把 nav_import.build_categories 的结果并入数据。

    mode=merge:   按分类名合并，链接按 url 去重后追加
    mode=replace: 清空现有分类后整体导入
    """
    if mode == "replace":
        data["categories"] = [
            {
                "id": _new_id(),
                "name": cat["name"],
                "links": [
                    {"id": _new_id(), "name": link["name"], "url": normalize_url(link["url"])}
                    for link in cat["links"]
                ],
            }
            for cat in categories
        ]
        return data

    for cat in categories:
        existing = next(
            (c for c in data["categories"] if c["name"] == cat["name"]), None
        )
        if existing is None:
            existing = {"id": _new_id(), "name": cat["name"], "links": []}
            data["categories"].append(existing)
        seen = {link["url"] for link in existing["links"]}
        for link in cat["links"]:
            url = normalize_url(link["url"])
            if url not in seen:
                seen.add(url)
                existing["links"].append(
                    {"id": _new_id(), "name": link["name"], "url": url}
                )
    return data
