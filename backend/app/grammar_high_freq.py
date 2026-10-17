"""第一篇 高频语法"""

CATEGORIES = [
    {
        "id": "high-freq",
        "name": "第一篇 高频语法",
        "items": [
            # ---------- 虚拟语气（3个子项） ----------
            {
                "id": "subjunctive-conditional",
                "title": "虚拟条件句",
                "summary": "表与事实相反的假设：现在虚拟（did/were）、过去虚拟（had done）、混合虚拟",
                "explanation": (
                    "虚拟条件句用来表达与事实相反的假设。分为三类："
                    "（1）现在虚拟：if 从句用 did/were，主句用 would/could/might + 动词原形，"
                    "表示与现在事实相反。"
                    "（2）过去虚拟：if 从句用 had done，主句用 would/could/might + have done，"
                    "表示与过去事实相反。"
                    "（3）混合虚拟：if 从句是过去时间，主句是现在影响，或反之。"
                    "注意：if 从句中 were 可以替代 was，且在正式文体中可将 if 省略并把 were/had/should 提到主语前（倒装）。"
                ),
                "examples": [
                    {"en": "If I were you, I would not do that.", "zh": "如果我是你，我不会那样做。（现在虚拟）"},
                    {"en": "If he had studied harder, he would have passed the exam.", "zh": "如果他当时更努力学习，他就会通过考试了。（过去虚拟）"},
                    {"en": "Were I you, I would accept the offer.", "zh": "要是我是你，我会接受这个录用。（if 省略+were倒装）"},
                ],
                "points": [
                    "现在虚拟：if + did/were，主句 would/could/might + 动词原形",
                    "过去虚拟：if + had done，主句 would/could/might + have done",
                    "were 可替代 was，且可与 if 连用或省略 if 实现倒装（Were I...）",
                    "mixed 虚拟：if 从句过去时间 + 主句现在结果，或反之",
                ],
                "mistakes": [
                    "❌ If I was you, I will do it.（混合了陈述语气和虚拟语气）",
                    "❌ If he studies hard, he would pass it.（时态不匹配）",
                ],
                "quiz": [
                    {
                        "q": "If I ______ you, I would buy a car.",
                        "options": ["am", "are", "were", "be"],
                        "answer": 2,
                        "tip": "现在虚拟，主语 I 用 were（虚拟语气专用）。"
                    },
                    {
                        "q": "If she ______ the truth, she would not have cried.",
                        "options": ["knew", "had known", "knows", "has known"],
                        "answer": 1,
                        "tip": "过去虚拟，if 从句用 had done，主句 would have done。"
                    },
                ],
            },
            {
                "id": "subjunctive-noun-clause",
                "title": "虚拟语气在名词性从句中的使用",
                "summary": "建议、命令、请求、决议等名词性从句中，谓语用 (should) + 动词原形",
                "explanation": (
                    "当主句谓语是 suggest, propose, recommend, insist, demand, request, order, advice 等"
                    "表示建议、命令、要求、决议的词时，从句谓语用 (should) + do。"
                    "英式英语常保留 should，美式英语常省略 should。"
                ),
                "examples": [
                    {"en": "The doctor suggested that he (should) stop smoking.", "zh": "医生建议他戒烟。"},
                    {"en": "It is important that everyone be present at the meeting.", "zh": "每个人都必须出席会议，这很重要。"},
                    {"en": "I insist that he leave immediately.", "zh": "我坚持他立刻离开。"},
                ],
                "points": [
                    "动词：suggest / propose / recommend / insist / demand / request / order / advise",
                    "结构：that + 主语 + (should) + 动词原形",
                    "形容词：important / necessary / essential / vital / urgent 等也可引导此类从句",
                    "美式常省略 should，英式常保留 should"
                ],
                "mistakes": [
                    "❌ He suggested that he stops smoking.（虚拟语气不用第三人称单数 stops）",
                    "❌ It is important that he is present.（应用 be，不受时态和人称限制）",
                ],
                "quiz": [
                    {
                        "q": "The teacher demanded that every student ______ on time.",
                        "options": ["comes", "come", "came", "will come"],
                        "answer": 1,
                        "tip": "demand 引导的从句谓语用 (should) + do，故用 come。"
                    },
                    {
                        "q": "It is necessary that she ______ the report by tomorrow.",
                        "options": ["finish", "finishes", "finished", "will finish"],
                        "answer": 0,
                        "tip": "necessary that 后接 (should) + do，故用 finish。"
                    },
                ],
            },
            {
                "id": "subjunctive-adverb-clause",
                "title": "虚拟语气在副词性从句中的使用",
                "summary": "as if / as though 引导的方式从句，表“好像／简直”，与事实相反用虚拟语气",
                "explanation": (
                    "as if / as though 引导方式从句，意为“好像／简直”。"
                    "如果从句的情况与主句事实相反，谓语要用虚拟语气："
                    "与现在事实相反 → 从句用 did/were；"
                    "与过去事实相反 → 从句用 had done。"
                    "如果与事实可能相符，则用陈述语气。"
                ),
                "examples": [
                    {"en": "He talks as if he knew everything.", "zh": "他说话好像无所不知。（实际上他不懂）"},
                    {"en": "She looks as though she had been crying.", "zh": "她看上去好像哭过。（实际上没哭过）"},
                    {"en": "He acts as if he is the boss.", "zh": "他表现得好像他是老板。（可能他真是老板，陈述语气）"},
                ],
                "points": [
                    "as if / as though = as though，引导方式从句",
                    "与现在事实相反 → 从句 did/were",
                    "与过去事实相反 → 从句 had done",
                    "与事实可能相符 → 用陈述语气"
                ],
                "mistakes": [
                    "❌ He talks as if he knows everything.（若他实际上不懂，应用 knew）",
                    "❌ She looks as if she cries.（主句是 looks，从句应用虚拟）",
                ],
                "quiz": [
                    {
                        "q": "He behaves as if he ______ the manager.",
                        "options": ["is", "were", "was", "be"],
                        "answer": 1,
                        "tip": "如果他实际上不是经理，用 were（与现在事实相反）。"
                    },
                    {
                        "q": "She looks as though she ______ ill for days.",
                        "options": ["has been", "had been", "is", "was"],
                        "answer": 1,
                        "tip": "与过去事实相反，从句用 had been。"
                    },
                ],
            },
            # ---------- 定语从句 ----------
            {
                "id": "attributive-clause",
                "title": "定语从句",
                "summary": "who / which / that 引导，修饰前面的名词；介词+which 结构",
                "explanation": (
                    "定语从句就像中文的“的”字，用来进一步说明前面名词的样子、身份或状态。"
                    "引导词选 who（指人）、which（指物）、that（人物皆可）。"
                    "先行词在从句里做主语时用 who/that，做宾语时可以用 whom/which/that，甚至可以省略。"
                    "介词+关系代词结构中，指物用 which，指人用 whom。"
                ),
                "examples": [
                    {"en": "This is the book that I bought yesterday.", "zh": "这是我昨天买的那本书。"},
                    {"en": "The man who lives next door is a doctor.", "zh": "隔壁住着的那位是医生。"},
                    {"en": "The room in which we met is small.", "zh": "我们会面的那个房间很小。（介词+which）"},
                ],
                "points": [
                    "先行词是人 → 用 who / that",
                    "先行词是物 → 用 which / that",
                    "先行词在从句里做宾语时，引导词可以省略（I like the book [that] you gave me）",
                    "介词+which 指物，介词+whom 指人",
                ],
                "mistakes": [
                    "❌ This is the book who I bought.（book 是物，不能用 who）",
                    "❌ This is the man which lives here.（人不能用 which）",
                ],
                "quiz": [
                    {
                        "q": "The girl ___ is standing there is my sister.",
                        "options": ["who", "which", "that"],
                        "answer": 0,
                        "tip": "girl 是人，且在从句里做主语，用 who。"
                    },
                    {
                        "q": "Is this the pen ___ you lost?",
                        "options": ["who", "which", "that"],
                        "answer": 1,
                        "tip": "pen 是物，用 which（that 也可，who 不行）。"
                    },
                ],
            },
            # ---------- 倒装结构 ----------
            {
                "id": "inversion",
                "title": "倒装结构",
                "summary": "部分倒装（否定/限定词提到句首）和完全倒装（地点/方位状语、there be）",
                "explanation": (
                    "部分倒装：否定或限定副词（never, seldom, rarely, hardly, little, not only, nowhere）"
                    "提到句首，句子要用部分倒装（助动词/be动词/情态动词 + 主语 + 谓语）。"
                    "完全倒张：地点/方位状语短语在句首，句子用完全倒装（谓语动词 + 主语）；"
                    "there be 句型也是完全倒装。"
                ),
                "examples": [
                    {"en": "Never have I seen such a beautiful scene.", "zh": "我从没见过这么美的景色。（部分倒装）"},
                    {"en": "Hardly had he arrived when it started to rain.", "zh": "他刚到，雨就下了起来。（部分倒装）"},
                    {"en": "On the wall hangs a picture.", "zh": "墙上挂着一幅画。（完全倒装）"},
                ],
                "points": [
                    "never / seldom / rarely / hardly / little / not only / nowhere 提到句首 → 部分倒装",
                    "地点状语在句首 → 完全倒装（谓语 + 主语）",
                    "there be 句型也是倒装结构",
                    "not only ... but also 连接主语时，第一分句用部分倒装"
                ],
                "mistakes": [
                    "❌ Never I have seen such a movie.（倒装后助动词要提到主语前）",
                    "❌ On the wall a picture hangs.（完全倒装应用 hangs a picture）",
                ],
                "quiz": [
                    {
                        "q": "_______ have I seen such a wonderful performance.",
                        "options": ["Never", "Ever", "Sometimes", "Often"],
                        "answer": 0,
                        "tip": "Never 提到句首，部分倒装，用 have I。"
                    },
                    {
                        "q": "_______ the teacher came in, the students stood up.",
                        "options": ["No sooner had", "No sooner did", "Hardly did", "Scarcely had"],
                        "answer": 0,
                        "tip": "No sooner had ... than ... 结构，部分倒装。"
                    },
                ],
            },
            # ---------- 非谓语动词 ----------
            {
                "id": "non-finite-infinitive",
                "title": "不定式 (to do)",
                "summary": "to + 动词原形，表目的、作主语、作宾语、作表语",
                "explanation": (
                    "不定式结构是 to + 动词原形。主要句法功能："
                    "1）作主语（To err is human.）；"
                    "2）作宾语（want / decide / hope / plan / agree 等动词后）；"
                    "3）作表语（My dream is to be a doctor.）；"
                    "4）表目的（相当于 in order to）。"
                    "否定形式在 to 前加 not（decide not to go）。"
                ),
                "examples": [
                    {"en": "To learn English well is not easy.", "zh": "把英语学好容易。（作主语）"},
                    {"en": "I want to go home.", "zh": "我想回家。（作宾语）"},
                    {"en": "I come here to study.", "zh": "我来这里是为了学习。（表目的）"},
                ],
                "points": [
                    "to do 表示目的时，可用 in order to 替换，意思更明确",
                    "want / decide / hope / plan / agree / refuse 等动词后常接 to do 作宾语",
                    "否定形式在 to 前加 not（decide not to go）",
                    "would love / like / prefer / hate 后接 to do 表示具体某一次"
                ],
                "mistakes": [
                    "❌ I want go home.（want 后要接 to do，缺了 to）",
                    "❌ He decided to not go.（not 应放在 to 前：decided not to go）",
                ],
                "quiz": [
                    {
                        "q": "She wants ___ a doctor.",
                        "options": ["be", "to be", "being"],
                        "answer": 1,
                        "tip": "want 后接 to do，所以用 to be。"
                    },
                    {
                        "q": "He came here ___ English.",
                        "options": ["learn", "to learn", "learning"],
                        "answer": 1,
                        "tip": "表目的，用 to learn。"
                    },
                ],
            },
            {
                "id": "non-finite-gerund",
                "title": "动名词 (doing)",
                "summary": "动词加 -ing 作名词，作主语、宾语、介词宾语",
                "explanation": (
                    "动名词是动词的 -ing 形式作名词用。常见句法功能："
                    "1）作主语（Swimming is good exercise.）；"
                    "2）作介词宾语（介词后面必须用动名词，如 good at / interested in / look forward to / about / without）；"
                    "3）作某些动词的宾语（enjoy / avoid / mind / practice / consider / suggest 等）。"
                    "与不定式作宾语的区别：某些动词后只能接动名词，如 enjoy / avoid / mind。"
                ),
                "examples": [
                    {"en": "Swimming keeps me fit.", "zh": "游泳让我保持健康。（作主语）"},
                    {"en": "I am interested in learning English.", "zh": "我对学习英语感兴趣。（介词宾语）"},
                    {"en": "I enjoy reading novels.", "zh": "我喜欢读小说。（作宾语）"},
                ],
                "points": [
                    "介词后面只能接动名词（to 作介词时除外，如 look forward to / be used to / object to）",
                    "enjoy / avoid / mind / practice / consider / suggest 等动词后接 doing",
                    "remember / forget / stop / try / regret 后接 doing 和 to do 意思不同",
                    "no smoking / no parking 等禁令用动名词"
                ],
                "mistakes": [
                    "❌ I am interested to learn English.（介词 in 后要用 doing）",
                    "❌ I enjoy to read novels.（enjoy 后只能接 doing）",
                ],
                "quiz": [
                    {
                        "q": "I am looking forward to ______ you soon.",
                        "options": ["meet", "meeting", "met", "meets"],
                        "answer": 1,
                        "tip": "look forward to 后面 to 是介词，要用 meeting。"
                    },
                    {
                        "q": "She enjoys ___ to music.",
                        "options": ["listen", "listening", "to listen", "listened"],
                        "answer": 1,
                        "tip": "enjoy 后面只能接 doing，故用 listening。"
                    },
                ],
            },
            {
                "id": "non-finite-participle",
                "title": "分词 (doing / done)",
                "summary": "现在分词表主动/进行，过去分词表被动/完成，作定语、表语、伴随状语",
                "explanation": (
                    "分词有现在分词（doing）和过去分词（done）两种形式。"
                    "现在分词表主动意义和进行意义（an interesting book）；"
                    "过去分词表被动意义和完成意义（a broken window）。"
                    "作定语时：单个分词放前面，短语放后面；"
                    "作表语时：主语是动作发出者用 doing，主语是动作承受者用 done；"
                    "独立主格结构也是分词的一种用法。"
                ),
                "examples": [
                    {"en": "The girl singing on the stage is my sister.", "zh": "舞台上唱歌的女孩是我姐姐。（现在分词作定语）"},
                    {"en": "The window broken by the storm needs repair.", "zh": "暴风雨打碎的窗户需要修理。（过去分词作定语）"},
                    {"en": "The boy stood there crying.", "zh": "男孩站在那儿哭着。（现在分词作伴随状语）"},
                ],
                "points": [
                    "-ing 表主动/进行，-ed 表被动/完成",
                    "单个分词作定语放前面，分词短语作定语放后面",
                    "作表语：主语是发出者用 -ing，主语是承受者用 -ed",
                    "interesting / bored, exciting / excited, tiring / tired 等一对词要区分"
                ],
                "mistakes": [
                    "❌ The movie was very interested.（电影不能感到有趣，应用 interesting）",
                    "❌ I saw him broke the window.（见证结构用 see sb do / doing，不接 broke）",
                ],
                "quiz": [
                    {
                        "q": "The book ______ on the desk is mine.",
                        "options": ["lying", "laid", "lay", "lie"],
                        "answer": 0,
                        "tip": "书在桌上躺着，主动用 lying。"
                    },
                    {
                        "q": "I am ______ in this movie.",
                        "options": ["interested", "interesting", "interest", "interests"],
                        "answer": 0,
                        "tip": "人感到感兴趣，用 interested。"
                    },
                ],
            },
            {
                "id": "non-finite-absolute",
                "title": "独立主格结构",
                "summary": "名词/代词 + 分词/形容词/副词/介词短语，作伴随状语，与句中主语无逻辑关系",
                "explanation": (
                    "独立主格结构（Nominative Absolute）结构：名词或代词（其所有格） + 分词 / 形容词 / 副词 / 介词短语。"
                    "它在句中作伴随状语，表示主句动作发生时的伴随情况。"
                    "独立主格与句子的主语没有逻辑上的主谓关系，所以要用独立主格而不是分词作状语。"
                    "常见形式：名词 + doing / done / 形容词 / 副词 / 介词短语。"
                ),
                "examples": [
                    {"en": "The meeting being over, we went home.", "zh": "会议结束后，我们回家了。（名词+doing）"},
                    {"en": "Weather permitting, we will go for a picnic.", "zh": "天气允许的话，我们会去野餐。（名词+分词）"},
                    {"en": "With his work done, he went out.", "zh": "工作做完后，他出去了。（With 独立主格）"},
                ],
                "points": [
                    "结构：名词/代词 + 分词 / 形容词 / 副词 / 介词短语",
                    "在句中作伴随状语，与句中主语无逻辑关系",
                    "With 独立主格结构常用于口语和非正式文体",
                    "分词的逻辑主语是独立主格中的名词，不是句子主语"
                ],
                "mistakes": [
                    "❌ The meeting being over, we went home.（此句正确，但若写成 Meeting being over... 缺冠词）",
                    "❌ With his work did, he went out.（done 应用过去分词，表示工作已完成）",
                ],
                "quiz": [
                    {
                        "q": "_______ the meeting was over, we left the room.",
                        "options": ["Since", "Because", "The meeting being over", "After"],
                        "answer": 2,
                        "tip": "独立主格结构作伴随状语，The meeting being over。"
                    },
                    {
                        "q": "With ______ finished, he went to bed.",
                        "options": ["homework", "his homework", "homework did", "his homework did"],
                        "answer": 1,
                        "tip": "With 独立主格：his homework（逻辑主语）+ finished（过去分词，被动/完成）。"
                    },
                ],
            },
            # ---------- It的用法 ----------
            {
                "id": "it-usage",
                "title": "It 的用法",
                "summary": "人称代词 it、形式主语 it（它做... / 使...）、形式宾语 it、强调结构 it is ... that ...",
                "explanation": (
                    "it 的常见用法："
                    "1）人称代词，指代前文提到的事物或动物；"
                    "2）作形式主语，用在 It is / was + 形容词 + to do / that 从句 / wh- 从句中，"
                    "真正的主语是后面的不定式或从句（It is important to learn English.）；"
                    "3）作形式宾语，用在 think / consider / find / make + it + 形容词 + to do 中，"
                    "真正的宾语是后面的不定式（I find it useful to read English every day.）；"
                    "4）强调结构：It is / was + 被强调部分 + that ...，强调主语、宾语或状语。"
                ),
                "examples": [
                    {"en": "It is raining.", "zh": "在下雨。（指代天气）"},
                    {"en": "It is important to learn English well.", "zh": "把英语学好很重要。（形式主语）"},
                    {"en": "I find it necessary to exercise every day.", "zh": "我发现每天锻炼很有必要。（形式宾语）"},
                    {"en": "It was Tom who broke the window.", "zh": "打碎窗户的是汤姆。（强调主语 Tom）"},
                ],
                "points": [
                    "人称代词 it：指代事物、动物、婴儿、时间、天气、距离等",
                    "形式主语：It is / was + 形容词 + to do / that 从句 / wh- 从句",
                    "形式宾语：think / consider / find / make / think + it + 形容词 + to do",
                    "强调结构：It is / was + 被强调部分 + that ...（强调时间/地点状语时 that 不可省略）"
                ],
                "mistakes": [
                    "❌ It is important learning English.（形式主语后要用 to do，不直接用 doing）",
                    "❌ It was Tom broke the window.（强调结构必须有 that）",
                ],
                "quiz": [
                    {
                        "q": "_____ is a pity that you missed the meeting.",
                        "options": ["It", "This", "That", "What"],
                        "answer": 0,
                        "tip": "形式主语 it，后面的 that 从句才是真正的主语内容。"
                    },
                    {
                        "q": "I consider ______ important to learn English.",
                        "options": ["it", "this", "that", "zero"],
                        "answer": 0,
                        "tip": "consider + it + 形容词 + to do，it 是形式宾语。"
                    },
                ],
            },
            # ---------- 状语从句 ----------
            {
                "id": "adverbial-clause",
                "title": "状语从句",
                "summary": "时间、地点、条件、目的、原因、结果、方式、让步、比较等各类状语从句",
                "explanation": (
                    "状语从句在句中修饰谓语动词、形容词或副词，表示时间、地点、原因、目的、结果、条件、让步、方式、比较等意义。"
                    "常见引导词："
                    "时间：when / while / as / before / after / since / until / once；"
                    "地点：where / wherever；"
                    "条件：if / unless / on condition that；"
                    "目的：so that / in order that；"
                    "原因：because / since / as / now that；"
                    "结果：so that（不能加 not）/ such ... that ...；"
                    "方式：as / as if / as though；"
                    "让步：although / though / even though / while / whereas / no matter + wh-；"
                    "比较：as ... as / not so ... as / than。"
                    "特别注意：时间和条件状语从句中，将来时要用一般现在时替代（If it rains tomorrow, I will stay at home.）。"
                ),
                "examples": [
                    {"en": "When I arrived, the meeting had already started.", "zh": "我到的时候，会议已经开始了。（时间）"},
                    {"en": "If it rains tomorrow, we will cancel the picnic.", "zh": "如果明天下雨，我们就取消野餐。（条件，用一般现在时替代将来时）"},
                    {"en": "He studied hard so that he could pass the exam.", "zh": "他努力学习，以便能通过考试。（目的）"},
                    {"en": "Although he is poor, he is honest.", "zh": "虽然他穷，但他诚实。（让步）"},
                ],
                "points": [
                    "时间/条件状语从句中，将来时要用一般现在时替代",
                    "so that 表目的，后面常接 can / could / may / might；so ... that ... 表结果，后面不用 not",
                    "although / though 虽然 ... 但 ...，与 but 不能连用",
                    "no matter + wh- = 无论 ... 都 ...，作让步状语从句",
                ],
                "mistakes": [
                    "❌ If it will rain tomorrow, I will stay at home.（时间/条件状语从句不能用将来时）",
                    "❌ Although he is poor, but he is happy.（although 与 but 不能连用）",
                ],
                "quiz": [
                    {
                        "q": "I will call you as soon as I ______ home.",
                        "options": ["arrive", "will arrive", "arrived", "have arrived"],
                        "answer": 0,
                        "tip": "时间状语从句中用一般现在时 replace 将来时，故用 arrive。"
                    },
                    {
                        "q": "_______ he is rich, he is not happy.",
                        "options": ["Although", "Because", "Since", "When"],
                        "answer": 0,
                        "tip": "虽然他富有，但他不快乐，让步状语从句用 Although。"
                    },
                ],
            },
            # ---------- 名词性从句 ----------
            {
                "id": "noun-clause",
                "title": "名词性从句",
                "summary": "主语从句、表语从句、宾语从句、同位语从句，在句中充当名词成分",
                "explanation": (
                    "名词性从句在句中充当名词的成分，分为四种："
                    "1）主语从句：作主语，常由 that / whether / wh- 引导（That he is late is certain.）；"
                    "2）表语从句：作系动词的表语，常由 that / whether / wh- 引导（The fact is that he is late.）；"
                    "3）宾语从句：作动词或介词的宾语，常由 that / whether / wh- 引导（I know that he is late.）；"
                    "4）同位语从句：解释说明前面名词的内容，常修饰 fact / news / idea / hope / possibility 等（The news that he is late is true.）。"
                    "引导词 that 在从句中不充当句子成分，只起连接作用，可在宾语从句中省略。"
                ),
                "examples": [
                    {"en": "That he is late is certain.", "zh": "他迟到是肯定的。（主语从句）"},
                    {"en": "The fact is that he is late.", "zh": "事实是他迟到了。（表语从句）"},
                    {"en": "I know that he is late.", "zh": "我知道他迟到了。（宾语从句）"},
                    {"en": "The news that he won the prize spread quickly.", "zh": "他获奖的消息很快传开了。（同位语从句）"},
                ],
                "points": [
                    "主语从句：that / whether / wh- 引导，that 不充当句子成分",
                    "表语从句：系动词后的从句，that 可省略吗？一般不省略，以免歧义",
                    "宾语从句：that / whether / wh- 引导，that 可省略（I know he is late.）",
                    "同位语从句：修饰 fact / news / idea / hope / possibility / report 等名词",
                ],
                "mistakes": [
                    "❌ That he is late is certain it.（主语从句前后不要重复主语）",
                    "❌ I know that he is late it.（宾语从句前后不要重复宾语）",
                ],
                "quiz": [
                    {
                        "q": "_____ he is late is certain.",
                        "options": ["It", "That", "What", "Whether"],
                        "answer": 1,
                        "tip": "主语从句，That 作引导词，不充当句子成分。"
                    },
                    {
                        "q": "I don't know ______ he will come.",
                        "options": ["if", "that", "which", "who"],
                        "answer": 0,
                        "tip": "宾语从句中，whether / if 引导选择疑问从句，用 if。"
                    },
                ],
            },
        ],
    },
]
