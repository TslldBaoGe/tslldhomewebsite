"""第三篇 挑战难句"""

CATEGORIES = [
    {
        "id": "challenge",
        "name": "第三篇 挑战难句",
        "items": [
            {
                "id": "challenge-01",
                "title": "难句01",
                "summary": "含定语从句、同位语从句、非谓语的长难句拆解",
                "explanation": (
                    "本句的主干是：The report was submitted. （报告被提交了。）"
                    "中间插入了多个修饰成分："
                    "1）that the manager wrote —— 同位语从句，解释说明 report 的内容；"
                    "2）which was discussed at the meeting —— 定语从句，修饰 report；"
                    "3）written by three employees —— 过去分词短语作定语，修饰 report。"
                    "拆解时先找到谓语 was submitted，再逐层剥开修饰成分。"
                ),
                "examples": [
                    {"en": "The report that the manager wrote, which was discussed at the meeting, written by three employees, was submitted on time.", "zh": "经经理撰写、在会议上讨论过、由三名员工书写的那份报告，按时提交了。"},
                ],
                "points": [
                    "先找主干：The report was submitted",
                    "that 从句作同位语，说明 report 的内容",
                    "which 从句作定语，修饰 report",
                    "written by ... 作过去分词短语定语",
                ],
                "mistakes": [
                    "❌ 把 which 从句误认为是独立句子，漏看它修饰 report",
                    "❌ 把 written 误认为是谓语动词，实际它是过去分词作定语",
                ],
                "quiz": [
                    {
                        "q": "本句中 that 从句的作用是？",
                        "options": ["定语从句", "同位语从句", "宾语从句", "状语从句"],
                        "answer": 1,
                        "tip": "that 从句解释说明 report 的内容，作同位语。"
                    },
                ],
            },
            {
                "id": "challenge-02",
                "title": "难句02",
                "summary": "含倒装结构和虚拟语气的长难句",
                "explanation": (
                    "本句：Not only did he finish the work, but he also did it well."
                    "not only ... but also 连接两个主语相同的分句，第一分句用部分倒装（did he finish）。"
                    "若把 not only 提到句首，第一分句必须用倒装结构。"
                ),
                "examples": [
                    {"en": "Not only did he finish the work, but he also did it well.", "zh": "他不仅完成了工作，而且做得很好。（部分倒装）"},
                ],
                "points": [
                    "not only ... but also 连接主语相同的两个分句，第一分句用部分倒装",
                    "not only 提到句首，助动词 did 提到主语前",
                ],
                "mistakes": [
                    "❌ Not only he finished the work, but he also did it well.（缺少倒装）",
                ],
                "quiz": [
                    {
                        "q": "本句中 did 的作用是？",
                        "options": ["实义动词", "助动词（构成倒装）", "情态动词", "系动词"],
                        "answer": 1,
                        "tip": "did 在这里是助动词，用于构成部分倒装结构。"
                    },
                ],
            },
        ],
    },
    {
        "id": "challenge-26-50",
        "name": "难句26~50",
        "items": [],
    },
]
