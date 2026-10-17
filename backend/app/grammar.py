"""英语语法知识库（自包含，无外部数据源）。

内容参考目录结构：
第一篇 高频语法：虚拟语气、定语从句、倒装结构、非谓语动词、It的用法、状语从句、名词性从句
第二篇 常考语法：基本句法、主谓一致、并列平行结构、省略、插入结构、否定结构、As的用法
第三篇 挑战难句：难句01~25、难句26~50
附录 基础语法：时态扫描、语态扫描、情态动词扫描、形容词副词及限定词、代词名词及数词、冠词、There be句型、强调句型

每个知识点结构：
{
  "id": 唯一标识,
  "title": 标题,
  "summary": 一句话说明,
  "explanation": 详细解释（中文）,
  "examples": [{"en": 英文例句, "zh": 中文翻译}],
  "points": [核心要点],
  "mistakes": [常见错点],
  "quiz": [{"q": 题目, "options": [选项], "answer": 正确选项索引, "tip": 解析}]
}
"""

from __future__ import annotations

import json
from pathlib import Path

# 各章节内容分模块存放，便于维护和扩展
from .grammar_basics import CATEGORIES as _BASICS
from .grammar_high_freq import CATEGORIES as _HIGH_FREQ
from .grammar_common import CATEGORIES as _COMMON
from .grammar_challenge import CATEGORIES as _CHALLENGE
from .grammar_appendix import CATEGORIES as _APPENDIX

SEED_FILE = Path(__file__).resolve().parent / "seed_grammar.json"


def _builtin() -> dict:
    categories = []
    categories.extend(_BASICS)
    categories.extend(_HIGH_FREQ)
    categories.extend(_COMMON)
    categories.extend(_CHALLENGE)
    categories.extend(_APPENDIX)
    return {"categories": categories}


def load_grammar() -> dict:
    if SEED_FILE.exists():
        try:
            data = json.loads(SEED_FILE.read_text(encoding="utf-8"))
            if isinstance(data.get("categories"), list):
                return data
        except (json.JSONDecodeError, OSError):
            pass
    return _builtin()


def find_item(grammar: dict, item_id: str):
    for cat in grammar["categories"]:
        for item in cat["items"]:
            if item["id"] == item_id:
                return cat, item
    return None, None
