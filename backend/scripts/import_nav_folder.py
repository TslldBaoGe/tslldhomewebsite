"""把本地文件夹里的书签/快捷方式导入导航板块（命令行版）。

用法 (在 backend 目录下):
  .venv/Scripts/python scripts/import_nav_folder.py <文件夹或书签HTML路径>

与网站「导航板块 → 编辑模式 → 从本地文件夹导入」走同一套解析逻辑
(app/nav_import.py)；区别是脚本直接写 seed 文件，随镜像发到服务器。
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import nav_import  # noqa: E402

SEED_FILE = Path(__file__).resolve().parents[1] / "app" / "seed_nav.json"


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    target = Path(sys.argv[1])
    if not target.exists():
        print(f"路径不存在: {target}")
        sys.exit(1)

    if target.is_file():
        groups = nav_import.parse_html_bookmarks(target)
        skipped: list[str] = []
    else:
        groups, skipped = nav_import.from_directory(target)

    categories = nav_import.build_categories(groups)
    if not categories:
        print("没有提取到任何链接（支持 .url/.desktop/.txt 及书签导出的 .html）")
        sys.exit(1)

    SEED_FILE.write_text(
        json.dumps({"categories": categories}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    total = sum(len(c["links"]) for c in categories)
    print(f"✅ 已写入 {SEED_FILE}")
    print(f"   {len(categories)} 个分类，共 {total} 条导航:")
    for c in categories:
        print(f"   - {c['name']}: {len(c['links'])} 条")
    if skipped:
        print(f"   跳过 {len(skipped)} 个无法识别的文件: {', '.join(skipped[:8])}")
    print("重启后端后生效；服务器上重新执行 deploy.sh 即可带上。")


if __name__ == "__main__":
    main()
