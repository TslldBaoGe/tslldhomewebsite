"""附录 基础语法 + 基础入门知识点"""

CATEGORIES = [
    {
        "id": "basics",
        "name": "基础语法",
        "items": [
            {
                "id": "be-verb",
                "title": "be 动词 (am / is / are)",
                "summary": "人称与 be 动词的对应关系，英语句子的基石",
                "explanation": (
                    "英语里几乎每个句子都需要一个谓语动词，be 动词（am/is/are）最常用。"
                    "它的核心作用是“是 / 在 / 有”，不表示动作，只表示状态或身份。"
                    "选择规则只看主语的人称和数量："
                ),
                "examples": [
                    {"en": "I am a student.", "zh": "我是学生。"},
                    {"en": "She is tall.", "zh": "她很高。"},
                    {"en": "They are friends.", "zh": "他们是朋友。"},
                ],
                "points": [
                    "主语用 I → 用 am",
                    "主语是 he / she / it 或单数名词 → 用 is",
                    "主语是 you / we / they 或复数名词 → 用 are",
                ],
                "mistakes": [
                    "❌ I is a student。（主语和动词不配对）",
                    "❌ She am tall。（人称用错了）",
                ],
                "quiz": [
                    {
                        "q": "He ___ my brother.",
                        "options": ["am", "is", "are"],
                        "answer": 1,
                        "tip": "主语 He 是第三人称单数，用 is。"
                    },
                    {
                        "q": "They ___ at home.",
                        "options": ["is", "are", "am"],
                        "answer": 1,
                        "tip": "主语 They 是第三人称复数，用 are。"
                    },
                ],
            },
            {
                "id": "simple-present",
                "title": "一般现在时",
                "summary": "表经常性动作或客观事实，第三人称单数动词加 -s",
                "explanation": (
                    "一般现在时不是“现在正在做”，而是表示习惯、经常性动作或永恒真理。"
                    "关键难点是第三人称单数（he / she / it）：实义动词要在末尾加 -s 或 -es。"
                ),
                "examples": [
                    {"en": "The earth moves around the sun.", "zh": "地球绕太阳转。"},
                    {"en": "He gets up at seven every day.", "zh": "他每天七点起床。"},
                    {"en": "I like English.", "zh": "我喜欢英语。"},
                ],
                "points": [
                    "主语不是第三人称单数 → 动词原形（I like / You like / They like）",
                    "主语是 he / she / it → 动词加 -s（He likes / She goes / It runs）",
                    "动词以 s / x / o / ch / sh 结尾 → 加 -es（go → goes, watch → watches）",
                ],
                "mistakes": [
                    "❌ He like music.（漏加 -s）",
                    "❌ She go to school.（漏加 -s）",
                ],
                "quiz": [
                    {
                        "q": "My father ___ coffee every morning.",
                        "options": ["drink", "drinks", "drinking"],
                        "answer": 1,
                        "tip": "father 是第三人称单数，drink 加 -s 变 drinks。"
                    },
                    {
                        "q": "The sun ___ in the east.",
                        "options": ["rise", "rises", "rose"],
                        "answer": 1,
                        "tip": "客观事实用一般现在时，sun 用 rises。"
                    },
                ],
            },
            {
                "id": "present-continuous",
                "title": "现在进行时",
                "summary": "be + doing，表示“现在正在做的事”",
                "explanation": (
                    "现在进行时结构是 am / is / are + 动词-ing，重点在“现在这个时刻”。"
                    "它和一般现在时最大的区别：一般现在时讲习惯，现在进行时讲此刻正在发生。"
                ),
                "examples": [
                    {"en": "Look! The baby is crying.", "zh": "看！宝宝在哭。"},
                    {"en": "We are studying English now.", "zh": "我们现在在学英语。"},
                    {"en": "He is not sleeping.", "zh": "他没有在睡觉。"},
                ],
                "points": [
                    "结构：主语 + am/is/are + 动词-ing",
                    "常伴 now / Look! / Listen! / at the moment 等副词",
                    "动词加 -ing 的拼写规则：e 尾去 e 加 ing（make → making），闭音节双写末字母（run → running）",
                ],
                "mistakes": [
                    "❌ He is sleep.（漏加 -ing）",
                    "❌ They is playing.（主谓不配）",
                ],
                "quiz": [
                    {
                        "q": "Listen! Someone ___ at the door.",
                        "options": ["knock", "is knocking", "knocks"],
                        "answer": 1,
                        "tip": "Listen! 提示此刻正在发生，用 is knocking。"
                    },
                    {
                        "q": "They ___ a game now.",
                        "options": ["play", "are playing", "plays"],
                        "answer": 1,
                        "tip": "now + 复数主语，用 are playing。"
                    },
                ],
            },
            {
                "id": "present-perfect",
                "title": "现在完成时",
                "summary": "have/has + 过去分词，表示过去动作对现在的影响或经历",
                "explanation": (
                    "现在完成时结构是 have / has + 过去分词。它的精髓是“过去做了，现在有影响或结果”，"
                    "或者“从过去一直做到现在”。常与 already / yet / just / ever / never / for / since 搭配。"
                ),
                "examples": [
                    {"en": "I have lost my keys.", "zh": "我钥匙丢了（现在找不到了）。"},
                    {"en": "She has been to Beijing.", "zh": "她去过北京。（有经历）"},
                    {"en": "We have lived here for five years.", "zh": "我们在这里住了五年了。（持续到现在）"},
                ],
                "points": [
                    "主语是 I / you / we / they → have + 过去分词",
                    "主语是 he / she / it → has + 过去分词",
                    "已经 / 刚才 → already / just；还没有 / 还 → yet（多用于疑问和否定）",
                ],
                "mistakes": [
                    "❌ I have gone to Paris.（表“去过”用 been，不是 gone）",
                    "❌ She has saw that movie.（过去分词用 saw，应为 seen）",
                ],
                "quiz": [
                    {
                        "q": "She ___ to London twice.",
                        "options": ["has gone", "has been", "went"],
                        "answer": 1,
                        "tip": "twice 表示经历，用 has been。"
                    },
                    {
                        "q": "I ___ my homework already.",
                        "options": ["have finished", "has finished", "finish"],
                        "answer": 0,
                        "tip": "I 用 have，past participle 是 finished。"
                    },
                ],
            },
            {
                "id": "there-be",
                "title": "There be 句型",
                "summary": "表示“有 / 存在”，be 动词跟名词的单复数配对",
                "explanation": (
                    "there be 句型用来引出“某地有某物或某人”。核心规则：be 动词必须跟"
                    "它后面紧跟的名词保持单复数一致，且名词通常不能用不定冠词 a/an 做主语（用 some / any / 数词等）。"
                ),
                "examples": [
                    {"en": "There is a book on the desk.", "zh": "桌子上有一本书。"},
                    {"en": "There are two apples in the bag.", "zh": "袋子里有两个苹果。"},
                    {"en": "There is some water in the cup.", "zh": "杯子里有一些水。"},
                ],
                "points": [
                    "后面名词是单数或不可数 → There is",
                    "后面名词是复数 → There are",
                    "疑问句把 is / are 提到句首：Is there a pen on the table?",
                ],
                "mistakes": [
                    "❌ There are a book on the table.（a book 是单数，应用 is）",
                    "❌ There is two students.（two students 是复数，应用 are）",
                ],
                "quiz": [
                    {
                        "q": "___ a cat under the table.",
                        "options": ["There is", "There are", "There be"],
                        "answer": 0,
                        "tip": "a cat 是单数，用 There is。"
                    },
                    {
                        "q": "___ many students in the classroom.",
                        "options": ["There is", "There are", "There be"],
                        "answer": 1,
                        "tip": "many students 是复数，用 There are。"
                    },
                ],
            },
        ],
    },
    {
        "id": "appendix",
        "name": "附录 基础语法",
        "items": [
            {
                "id": "appendix-tense",
                "title": "时态扫描",
                "summary": "一般现在时、现在进行时、现在完成时、一般过去时、一般将来时等快速对照",
                "explanation": (
                    "英语主要时态可分为四大时态（一般、进行、完成、完成进行）× 三大时间（过去、现在、将来），"
                    "共 12 种。基础学习重点掌握：一般现在时（习惯/真理）、现在进行时（此刻正在）、"
                    "现在完成时（过去对现在的影响）、一般过去时（过去的事）、一般将来时（将要发生）。"
                    "关键是判断“时间状语”和“动作与现在的关系”。"
                ),
                "examples": [
                    {"en": "I work here. I am working now. I have worked here for 3 years.", "zh": "我在这里工作。我现在正在工作。我在这里工作了3年了。"},
                    {"en": "I worked there last year. I will work there tomorrow.", "zh": "我去年在那里工作。我明天将在那里工作。"},
                ],
                "points": [
                    "一般现在时：表示习惯、真理，常与 always / usually / every day 搭配",
                    "现在进行时：表示此刻正在，常与 now / at the moment 搭配",
                    "现在完成时：强调对现在的影响，常与 already / yet / for / since 搭配",
                    "一般过去时：表示过去发生的动作，常与 yesterday / last week / in 2020 搭配",
                    "一般将来时：will / be going to + 动词原形",
                ],
                "mistakes": [
                    "❌ I am work here.（现在进行时不能用于状态类习惯）",
                    "❌ I have worked here yesterday.（完成时不能与过去时间状语连用）",
                ],
                "quiz": [
                    {
                        "q": "I ______ English for three years.",
                        "options": ["learn", "am learning", "have learned", "learned"],
                        "answer": 2,
                        "tip": "for three years 表示持续到现在，用现在完成时 have learned。"
                    },
                    {
                        "q": "She ______ to the cinema last night.",
                        "options": ["goes", "went", "has gone", "will go"],
                        "answer": 1,
                        "tip": "last night 是过去时间状语，用一般过去时 went。"
                    },
                ],
            },
            {
                "id": "appendix-voice",
                "title": "语态扫描",
                "summary": "主动语态与被动语态的转换，be + 过去分词",
                "explanation": (
                    "语态表示动作的发出者与承受者的关系。主动语态：主语是动作发出者；"
                    "被动语态：主语是动作承受者。被动语态结构：be + 过去分词（by + 施动者）。"
                    "只有及物动词才能用被动语态。常用时态的被动："
                    "一般现在时被动 am/is/are + done；一般过去时被动 was/were + done；"
                    "现在完成时被动 have/has + been + done；情态动词被动 can/must + be + done。"
                ),
                "examples": [
                    {"en": "The teacher teaches English. English is taught by the teacher.", "zh": "老师教英语。英语被老师教。"},
                    {"en": "They built the house last year. The house was built last year.", "zh": "他们去年建了这栋房子。这栋房子去年被建成了。"},
                ],
                "points": [
                    "被动语态：be + 过去分词",
                    "只能把及物动词的主动句变成被动句",
                    "不想提施动者时可省略 by + 人",
                    "常考：情态动词被动（should be done）、现在完成时被动（has been done）"
                ],
                "mistakes": [
                    "❌ The book was wrote by him.（被动要用过去分词 written，不是 wrote）",
                    "❌ He is gone.（gone 是不及物动词过去分词，不能构成被动语态）",
                ],
                "quiz": [
                    {
                        "q": "The window ______ by the boy yesterday.",
                        "options": ["break", "broke", "was broken", "is broken"],
                        "answer": 2,
                        "tip": "昨天被男孩打破的窗户，一般过去时被动 was broken。"
                    },
                    {
                        "q": "English ______ all over the world.",
                        "options": ["speak", "speaks", "is spoken", "is speaking"],
                        "answer": 2,
                        "tip": "英语被全世界说，一般现在时被动 is spoken。"
                    },
                ],
            },
            {
                "id": "appendix-modal",
                "title": "情态动词扫描",
                "summary": "can / could / may / might / must / should / would 等，后接动词原形",
                "explanation": (
                    "情态动词表达说话人的态度：能力（can / could）、许可（may / can）、"
                    "可能性（may / might / could）、义务 / 必要（must / should / ought to）、"
                    "意愿（will / would）。情态动词后面永远接动词原形，不加 -s，"
                    "也没有过去时变化（除了 could / would / might 作为过去时形式）。"
                ),
                "examples": [
                    {"en": "She can speak three languages.", "zh": "她会说三种语言。（能力）"},
                    {"en": "You must wear a seatbelt.", "zh": "你必须系安全带。（义务）"},
                    {"en": "It might rain tomorrow.", "zh": "明天可能会下雨。（可能性）"},
                ],
                "points": [
                    "情态动词 + 动词原形，不加 to",
                    "第三人称单数不加 -s（He can swim，不是 He cans swim）",
                    "没有不定式和分词形式，不能和其他情态动词连用",
                    "must 表主观强义务，have to 表客观必要"
                ],
                "mistakes": [
                    "❌ He can to swim.（情态动词后不要加 to）",
                    "❌ She cans dance.（第三人称单数不加 -s）",
                ],
                "quiz": [
                    {
                        "q": "You ______ smoke here. It's forbidden.",
                        "options": ["must", "must not", "can", "may"],
                        "answer": 1,
                        "tip": "这里禁止吸烟，表禁止用 must not。"
                    },
                    {
                        "q": "_____ I use your phone?",
                        "options": ["Must", "Can", "Should", "Ought"],
                        "answer": 1,
                        "tip": "请求许可用 Can I...？"
                    },
                ],
            },
            {
                "id": "appendix-articles",
                "title": "冠词",
                "summary": "a / an（不定冠词）、the（定冠词）、零冠词的用法区别",
                "explanation": (
                    "冠词是限定词的一种。不定冠词 a / an 泛指一类或一个不特定的事物；"
                    "定冠词 the 特指说话者和听话者都知道的特定人或事物；"
                    "零冠词（不用冠词）常用于不可数名词、复数名词泛指、专有名词等。"
                    "a 用于辅音音素开头，an 用于元音音素开头（如 a university，an hour）。"
                ),
                "examples": [
                    {"en": "I saw a dog in the park. The dog was black.", "zh": "我在公园看见一条狗。那条狗是黑色的。（第一次泛指，第二次特指）"},
                    {"en": "The sun rises in the east.", "zh": "太阳从东边升起。（独一无二，用 the）"},
                    {"en": "I like music.", "zh": "我喜欢音乐。（不可数名词泛指，零冠词）"},
                ],
                "points": [
                    "a / an：第一次提及，泛指任意一个",
                    "the：特指某一特定人或事，或前文提到过的人或事",
                    "零冠词：不可数名词泛指、复数名词泛指、人名地名等",
                    "a university / an hour：按发音而非字母选择 a/an"
                ],
                "mistakes": [
                    "❌ I saw a moon last night.（月亮独一无二，用 the moon）",
                    "❌ She is a teacher. A teacher is kind.（第二次提及应用 the teacher）",
                ],
                "quiz": [
                    {
                        "q": "_____ moon goes around _____ earth.",
                        "options": ["The, the", "A, an", "A, the", "The, an"],
                        "answer": 0,
                        "tip": "月亮和地球都是独一无二的，都用 the。"
                    },
                    {
                        "q": "I want to buy ______ umbrella.",
                        "options": ["a", "an", "the", "zero"],
                        "answer": 1,
                        "tip": "umbrella 以元音音素开头，用 an umbrella。"
                    },
                ],
            },
        ],
    },
]
