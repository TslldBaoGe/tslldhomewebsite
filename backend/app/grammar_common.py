"""第二篇 常考语法"""

CATEGORIES = [
    {
        "id": "common",
        "name": "第二篇 常考语法",
        "items": [
            # ---------- 基本句法 ----------
            {
                "id": "basic-syntax",
                "title": "基本句法",
                "summary": "简单句、并列句、复合句的结构与识别",
                "explanation": (
                    "英语句子按结构分为三类："
                    "1）简单句：只有一个主谓结构（The sun rises in the east.）；"
                    "2）并列句：两个或两个以上地位相等的句子，用 and / but / or / so / yet 等并列连词连接（I like tea, and she likes coffee.）；"
                    "3）复合句：主句和从句，用 because / if / that / which / who 等从属连词或关系代词连接（I know that he is busy.）。"
                    "识别关键：数主谓结构的数量和它们之间的连接方式。"
                ),
                "examples": [
                    {"en": "The earth moves around the sun.", "zh": "地球绕太阳转。（简单句）"},
                    {"en": "I like tea, and she likes coffee.", "zh": "我喜欢茶，她喜欢咖啡。（并列句）"},
                    {"en": "I know that he is busy.", "zh": "我知道他很忙。（复合句）"},
                ],
                "points": [
                    "简单句：一个主谓结构",
                    "并列句：两个及以上主谓结构，并列连词连接，地位相等",
                    "复合句：主句 + 从句，从属连词/关系代词连接，地位不相等",
                    "识别时先找谓语动词，再判断主谓结构数量"
                ],
                "mistakes": [
                    "❌ I like tea and she likes coffee.（并列句前最好加逗号）",
                    "❌ I know he is busy he is a student.（两个从句不能直接并列，需加连词）",
                ],
                "quiz": [
                    {
                        "q": "I like music, ______ my sister likes pop songs.",
                        "options": ["and", "because", "that", "if"],
                        "answer": 0,
                        "tip": "两个分句地位相等，用并列连词 and。"
                    },
                    {
                        "q": "I know ______ he is here.",
                        "options": ["that", "and", "but", "or"],
                        "answer": 0,
                        "tip": "that 引导宾语从句，作 know 的宾语。"
                    },
                ],
            },
            # ---------- 主谓一致 ----------
            {
                "id": "subject-verb-agreement",
                "title": "主谓一致",
                "summary": "主语和谓语动词在人称和数上要保持一致",
                "explanation": (
                    "主谓一致的核心原则：就近原则（there be / 选择疑问词作主语时）、不定代词作主语、"
                    "名词作主语时的数词判断。常见考点："
                    "（1）there be 句型：be 动词跟就近的主语保持单复数一致；"
                    "（2）不定代词：everybody / anyone / nobody / each / either / neither 视为单数；some / any / all / most 看后面名词；"
                    "（3）连接词：and 连接两个单数名词 → 复数；or / either ... or / neither ... nor → 就近原则；"
                    "（4）集合名词：作为整体时单数，作为个体时复数。"
                ),
                "examples": [
                    {"en": "There is a book and two pens on the desk.", "zh": "桌子上有一本书和两支钢笔。（就近原则）"},
                    {"en": "Everybody is here.", "zh": "每个人都到了。（不定代词 everybody 视为单数）"},
                    {"en": "Tom and Jerry are good friends.", "zh": "汤姆和杰里是好朋友。（and 连接，用复数）"},
                ],
                "points": [
                    "there be 句型：be 动词跟就近的主语一致",
                    "everybody / anyone / nobody / each / either / neither 视为单数",
                    "and 连接两个单数名词 → 谓语用复数",
                    "or / either ... or / neither ... nor → 谓语跟就近的主语一致"
                ],
                "mistakes": [
                    "❌ There is two students.（就近原则，应用 are）",
                    "❌ Everybody are here.（everybody 视为单数，应用 is）",
                ],
                "quiz": [
                    {
                        "q": "There ______ a book and two pens on the desk.",
                        "options": ["is", "are", "be", "being"],
                        "answer": 1,
                        "tip": "there be 句型，be 动词跟就近的主语 pens（复数）一致，用 are。"
                    },
                    {
                        "q": "Either Tom or Jerry ______ right.",
                        "options": ["is", "are", "be"],
                        "answer": 0,
                        "tip": "either ... or ... 采用就近原则，Jerry 是单数，用 is。"
                    },
                ],
            },
            # ---------- 并列平行结构 ----------
            {
                "id": "parallel-structure",
                "title": "并列平行结构",
                "summary": "并列连词连接的成分词性必须一致",
                "explanation": (
                    "并列平行结构要求：用 and / or / but / not only ... but also / either ... or / neither ... nor"
                    "连接的成分，词性必须一致（名词并名词、动词并动词、形容词并形容词、不定式并不定式、动名词并动名词等）。"
                    "常见错误：把名词并形容词，把不定式并动名词。"
                ),
                "examples": [
                    {"en": "She likes swimming and reading.", "zh": "她喜欢游泳和阅读。（动名词并动名词）"},
                    {"en": "He is handsome and kind.", "zh": "他既英俊又善良。（形容词并形容词）"},
                    {"en": "My job is to teach English and to write books.", "zh": "我的工作是教英语和写书。（不定式并不定式）"},
                ],
                "points": [
                    "and / or / but 连接的成分词性必须相同",
                    "not only ... but also / either ... or / neither ... nor 连接的成分词性也必须相同",
                    "常见错误：to do 并 doing，名词并形容词，动词并形容词",
                ],
                "mistakes": [
                    "❌ She likes swimming and to read.（动名词并不定式，错误）",
                    "❌ He is handsome and a doctor.（形容词并名词，错误）",
                ],
                "quiz": [
                    {
                        "q": "She likes ______ and ______.",
                        "options": ["swim, read", "swimming, to read", "swimming, reading", "swim, reading"],
                        "answer": 2,
                        "tip": "两个动名词并列，用 swimming, reading。"
                    },
                    {
                        "q": "His job is to teach English and ______ books.",
                        "options": ["write", "writing", "to write", "wrote"],
                        "answer": 2,
                        "tip": "to teach 并 to write，to 可省略，故用 write（或 to write）。"
                    },
                ],
            },
            # ---------- 省略 ----------
            {
                "id": "ellipsis",
                "title": "省略",
                "summary": "避免重复，省略主语、谓语、宾语等成分",
                "explanation": (
                    "省略是为了避免语言的重复和冗赘。常见省略类型："
                    "1）比较级/最高级结构中的省略（She is taller than I am [tall].）；"
                    "2）比较级/最高级结构中的省略（She is taller than I am [tall].）；"
                    "3）不定式和动名词作宾语时的省略（I want to go [there].）；"
                    "4）关系代词在定语从句中作宾语时可省略（The book [that] I bought.）；"
                    "5）时间/条件状语从句中主语 + be 动词的省略（When [you are] in Rome, do as the Romans do.）。"
                ),
                "examples": [
                    {"en": "She is taller than I am.", "zh": "她比我高。（省略了 tall）"},
                    {"en": "The book I bought is interesting.", "zh": "我买的那本书很有趣。（省略了 that）"},
                    {"en": "If necessary, call me.", "zh": "如果需要，给我打电话。（省略了 it is）"},
                ],
                "points": [
                    "比较级/最高级结构中，后半部分可省略重复部分",
                    "关系代词在定语从句中作宾语时可省略",
                    "不定式/动名词作宾语补足语时，可省略不必要部分",
                    "时间/条件/让步状语从句中，主语 + be 动词可省略"
                ],
                "mistakes": [
                    "❌ She is taller than me.（口语可用，书面语中比较级后用主格 I am [tall]）",
                    "❌ The book I bought it is informative.（定语从句中不得重复宾语 it）",
                ],
                "quiz": [
                    {
                        "q": "The book ______ I bought is interesting.",
                        "options": ["that", "which", "who", "zero"],
                        "answer": 3,
                        "tip": "that / which 作定语从句宾语时可省略。"
                    },
                    {
                        "q": "She is taller than I ______.",
                        "options": ["am", "is", "are", "zero"],
                        "answer": 0,
                        "tip": "比较级从句中省略了 am tall，完整形式为 than I am tall。"
                    },
                ],
            },
            # ---------- 插入结构 ----------
            {
                "id": "insertion",
                "title": "插入结构",
                "summary": "插入语在句中不作句子成分，用逗号隔开",
                "explanation": (
                    "插入结构（插入语）在句中不担任任何语法成分，只表示说话人的语气、态度或顺接等含义，"
                    "用逗号与句子其他部分隔开。常见插入语："
                    "1）表示语气：of course / certainly / surely / perhaps / maybe / luckily / unfortunately / honestly；"
                    "2）表示顺接：then / therefore / however / otherwise / besides / meanwhile；"
                    "3）人称代词 + 说话动词：I think / I believe / in my opinion / to be honest。"
                    "插入语在句首、句中、句尾皆可，句中时前后都要用逗号隔开。"
                ),
                "examples": [
                    {"en": "Of course, I will help you.", "zh": "当然，我会帮你。（句首）"},
                    {"en": "He is, of course, right.", "zh": "他当然是对的。（句中）"},
                    {"en": "I think, therefore I am.", "zh": "我想，故我在。（插入语）"},
                ],
                "points": [
                    "插入语在句中不作句子成分",
                    "用逗号与句子其他部分隔开",
                    "句中插入语前后都要加逗号",
                    "去掉插入语后，句子仍应是完整的"
                ],
                "mistakes": [
                    "❌ He is of course right.（句中插入语缺少逗号）",
                    "❌ I think he is right.（此句中 I think 是插入语，可省略）",
                ],
                "quiz": [
                    {
                        "q": "_______, he is a good student.",
                        "options": ["Of course", "However", "Therefore", "Luckily"],
                        "answer": 0,
                        "tip": "句首插入语，用逗号隔开。"
                    },
                    {
                        "q": "He is ______ a good student.",
                        "options": ["of course", "therefore", "however", "otherwise"],
                        "answer": 0,
                        "tip": "句中插入语，前后加逗号。"
                    },
                ],
            },
            # ---------- 否定结构 ----------
            {
                "id": "negation",
                "title": "否定结构",
                "summary": "不完全否定、双重否定、否定词提到句首的半倒装",
                "explanation": (
                    "否定结构包括："
                    "1）不完全否定：not all / not both / not always / not entirely 等，表示“不是全部/都/总是”；"
                    "2）双重否定：not ... no / never / nobody / nothing / nowhere 等，两个否定共表示肯定；"
                    "3）否定词提到句首：never / seldom / rarely / hardly / little / no sooner / nowhere 等，"
                    "句子要用部分倒装。"
                ),
                "examples": [
                    {"en": "Not all students like math.", "zh": "不是所有学生都喜欢数学。（不完全否定）"},
                    {"en": "I can't do nothing.", "zh": "我不能一事无做。（双重否定，表肯定）"},
                    {"en": "Never have I seen such a thing.", "zh": "我从未见过这样的事。（否定词提到句首，倒装）"},
                ],
                "points": [
                    "not all ≠ all ... not：not all 表示“不是全部”，all ... not 也表示“不是全部”",
                    "双重否定共表示肯定（I can't do nothing = I must do something）",
                    "否定词（never / seldom / rarely / hardly / little / no sooner / nowhere）提到句首，部分倒装",
                    "little / few 本身带否定意义，little = almost none"
                ],
                "mistakes": [
                    "❌ All students don't like math.（表所有学生都不喜欢，若想表“不是全部”，应用 Not all students like math.）",
                    "❌ I can't do anything.（此句正确，表示我一事都不能做；若与 I can't do nothing 比较，前者是单否定，后者是双重否定）",
                ],
                "quiz": [
                    {
                        "q": "_______ have I seen such a wonderful movie.",
                        "options": ["Never", "Ever", "Always", "Often"],
                        "answer": 0,
                        "tip": "Never 提到句首，部分倒装。"
                    },
                    {
                        "q": "Not ______ students passed the exam.",
                        "options": ["all", "both", "every", "each"],
                        "answer": 0,
                        "tip": "not all 表示“不是全部”，用 all。"
                    },
                ],
            },
            # ---------- As 的用法 ----------
            {
                "id": "as-usage",
                "title": "As 的用法",
                "summary": "as 作连词（如同/当/因为）、关系代词（如同...的）、介词（作为）",
                "explanation": (
                    "as 是多功能词："
                    "1）作连词：如同（as if / as though）、当……的时候（as / when）、因为（as / since / because，较弱）；"
                    "2）作关系代词：such ... as（像……那样的）、the same ... as（和……一样的）；"
                    "3）作介词：作为（as a teacher / as known / as far as I know）。"
                    "常见固定搭配：as soon as（一……就……）、as long as（只要/只要……）、as far as I know（就我所知）、as a result（结果）、as well as（以及）。"
                ),
                "examples": [
                    {"en": "As I was walking down the street, I met an old friend.", "zh": "我走在街上时，遇到了一个老朋友。（as = 当……时候）"},
                    {"en": "She is as beautiful as her mother.", "zh": "她和她母亲一样漂亮。（as ... as ... 等比级）"},
                    {"en": "He works as a teacher.", "zh": "他作为一名老师工作。（as 作介词）"},
                    {"en": "Such people as you are rare.", "zh": "像你这样的人很少。（such ... as 关系代词）"},
                ],
                "points": [
                    "as if / as though：好像，引导方式从句",
                    "as soon as：一……就……",
                    "as long as：只要……",
                    "as far as I know：就我所知",
                    "as a teacher：作为一名老师",
                    "such ... as / the same ... as：关系代词用法"
                ],
                "mistakes": [
                    "❌ He works like a teacher.（like 是介词，后面不能接从句；若表“担任……职务”，用 as）",
                    "❌ Such a man as you is rare.（应用 such people as you，复数一致）",
                ],
                "quiz": [
                    {
                        "q": "He works ______ a teacher.",
                        "options": ["like", "as", "of", "for"],
                        "answer": 1,
                        "tip": "表“担任……职务”，用 as a teacher。"
                    },
                    {
                        "q": "_______ I know, he is a good man.",
                        "options": ["As far as", "Such as", "As well as", "As soon as"],
                        "answer": 0,
                        "tip": "as far as I know = 就我所知。"
                    },
                ],
            },
        ],
    },
]
