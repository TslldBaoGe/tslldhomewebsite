"""英语 12 大时态详解（替换原“时态扫描”总览）"""

CATEGORIES = [
    {
        "id": "tense",
        "name": "时态详解",
        "items": [
            {
                "id": "tense-simple-present",
                "title": "一般现在时",
                "summary": "动词原形 / 三单加 -s，表习惯、真理、事实、状态",
                "explanation": (
                    "一般现在时表示经常性、习惯性的动作或客观真理，与“现在正在做”无关。"
                    "结构：主语 + 动词原形（主语是第三人称单数时动词加 -s/-es）。"
                    "常见时间状语：always, usually, often, sometimes, every day, on Sundays。"
                    "特殊用法：① 表客观真理（The earth moves around the sun.）；"
                    "② 表现在状态（I know him.）；③ 在时间/条件状语从句中代替将来时（If it rains tomorrow...）。"
                ),
                "examples": [
                    {"en": "I get up at six every morning.", "zh": "我每天早上六点起床。（习惯）"},
                    {"en": "The sun rises in the east.", "zh": "太阳从东方升起。（真理）"},
                    {"en": "She works in a hospital.", "zh": "她在一家医院工作。（现在的状态）"},
                ],
                "points": [
                    "主语是 he/she/it 或单数名词 → 动词加 -s（work → works）",
                    "以 s/x/o/ch/sh 结尾 → 加 -es（go → goes, watch → watches）",
                    "辅音+y 结尾 → 变 y 为 i 加 -es（study → studies）",
                    "否定句用 don't/doesn't + 动词原形；疑问句用 Do/Does 开头",
                ],
                "mistakes": [
                    "❌ He like music.（漏加 -s，应为 He likes）",
                    "❌ Does he likes music?（Does 后动词要用原形 likes → like）",
                ],
                "quiz": [
                    {
                        "q": "My sister ___ to school by bus every day.",
                        "options": ["go", "goes", "going", "went"],
                        "answer": 1,
                        "tip": "sister 是第三人称单数，且 every day 表习惯，用 goes。"
                    },
                    {
                        "q": "___ your father ___ newspapers every morning?",
                        "options": ["Do, read", "Does, read", "Does, reads", "Is, reading"],
                        "answer": 1,
                        "tip": "第三人称单数疑问句用 Does 开头，后面动词还原为 read。"
                    },
                ],
            },
            {
                "id": "tense-simple-past",
                "title": "一般过去时",
                "summary": "动词过去式，表过去某时间发生的动作或状态",
                "explanation": (
                    "一般过去时表示过去某个时间发生的动作或存在的状态，与现在没有联系。"
                    "结构：主语 + 动词过去式。规则动词加 -ed，不规则动词需单独记忆"
                    "（go → went, see → saw, buy → bought, take → took）。"
                    "常见时间状语：yesterday, last week, in 2020, three days ago, just now。"
                    "否定句用 didn't + 动词原形；疑问句用 Did 开头。"
                ),
                "examples": [
                    {"en": "I visited my grandmother last Sunday.", "zh": "我上周日去看望了奶奶。"},
                    {"en": "He bought a new phone two days ago.", "zh": "他两天前买了一部新手机。"},
                    {"en": "She didn't come to the party yesterday.", "zh": "她昨天没来参加聚会。"},
                ],
                "points": [
                    "规则动词加 -ed；以 e 结尾只加 -d（live → lived）",
                    "辅音+y 结尾 → 变 y 为 i 加 -ed（study → studied）",
                    "重读闭音节结尾 → 双写末字母加 -ed（stop → stopped）",
                    "didn't / Did 后面动词一律还原为原形",
                ],
                "mistakes": [
                    "❌ I didn't went there.（didn't 后要用原形 go）",
                    "❌ Did you saw the film?（Did 后要用原形 see）",
                ],
                "quiz": [
                    {
                        "q": "They ___ a great time at the party last night.",
                        "options": ["have", "had", "has", "having"],
                        "answer": 1,
                        "tip": "last night 是过去时间状语，have 的过去式是 had。"
                    },
                    {
                        "q": "___ you ___ your homework yesterday evening?",
                        "options": ["Did, finish", "Do, finish", "Did, finished", "Were, finish"],
                        "answer": 0,
                        "tip": "过去时疑问句用 Did 开头，后面动词用原形 finish。"
                    },
                ],
            },
            {
                "id": "tense-simple-future",
                "title": "一般将来时",
                "summary": "will + 动词原形 或 be going to + 动词原形，表将要发生",
                "explanation": (
                    "一般将来时表示将来要发生的动作或状态。两种主要结构："
                    "① will + 动词原形：表示临时决定、预测、承诺（I will help you. It will rain.）；"
                    "② be going to + 动词原形：表示事先有计划、或有明显迹象将要发生"
                    "（I am going to buy a car. Look at the clouds — it is going to rain.）。"
                    "常见时间状语：tomorrow, next week, soon, in the future。"
                ),
                "examples": [
                    {"en": "I will call you tomorrow.", "zh": "我明天给你打电话。（临时决定）"},
                    {"en": "She is going to study abroad next year.", "zh": "她打算明年出国留学。（已有计划）"},
                    {"en": "Look at those black clouds. It is going to rain.", "zh": "看那些乌云，要下雨了。（有迹象）"},
                ],
                "points": [
                    "will / shall + 动词原形，各人称通用（shall 多用于第一人称疑问句）",
                    "be going to 表计划或有迹象的将来",
                    "时间/条件状语从句中用一般现在时代替将来时（When he comes, I will tell him.）",
                    "祈使句 + and/or + 将来时句子（Hurry up, or you will be late.）",
                ],
                "mistakes": [
                    "❌ I will call you when he will come tomorrow.（时间从句要用 comes）",
                    "❌ She is go to travel next month.（应为 is going to travel）",
                ],
                "quiz": [
                    {
                        "q": "Look at the dark sky. It ___ rain.",
                        "options": ["will", "is going to", "would", "was going to"],
                        "answer": 1,
                        "tip": "有迹象表明将要发生，用 be going to。"
                    },
                    {
                        "q": "I ___ you with your English this weekend.",
                        "options": ["will help", "am going help", "help", "helped"],
                        "answer": 0,
                        "tip": "临时决定的将来动作用 will help。"
                    },
                ],
            },
            {
                "id": "tense-past-future",
                "title": "过去将来时",
                "summary": "would + 动词原形 / was going to，从过去看将要发生",
                "explanation": (
                    "过去将来时表示从过去某一时间看，将来要发生的动作或状态。"
                    "结构：would + 动词原形，或 was/were going to + 动词原形。"
                    "常见于宾语从句中，主句是过去时（He said he would come.）。"
                    "常见时间状语：the next day, the following week。"
                ),
                "examples": [
                    {"en": "He said he would come the next day.", "zh": "他说他第二天会来。"},
                    {"en": "I was going to leave when the phone rang.", "zh": "我正要离开，电话响了。"},
                    {"en": "She told me she would be fifteen the next month.", "zh": "她告诉我她下个月就十五岁了。"},
                ],
                "points": [
                    "would + do，或 was/were going to + do",
                    "主要用于宾语从句，主句谓语是过去时",
                    "表示过去某个时间之后的安排或打算",
                ],
                "mistakes": [
                    "❌ He said he will come the next day.（主句是 said，从句要用 would come）",
                    "❌ I was going to leave when the phone rang.（此句正确，需注意 ring 用过去式）",
                ],
                "quiz": [
                    {
                        "q": "She said she ___ buy a new bike the next week.",
                        "options": ["will", "would", "is going to", "buys"],
                        "answer": 1,
                        "tip": "主句 said 是过去时，从句表示从过去看将来，用 would。"
                    },
                    {
                        "q": "We ___ start when it began to rain.",
                        "options": ["were about to", "were going to", "will", "are going to"],
                        "answer": 1,
                        "tip": "过去将来时表示过去打算做某事，用 were going to。"
                    },
                ],
            },
            {
                "id": "tense-present-continuous",
                "title": "现在进行时",
                "summary": "am/is/are + doing，表现此时此刻正在进行",
                "explanation": (
                    "现在进行时表示现在这一时刻或现阶段正在进行的动作。"
                    "结构：主语 + am/is/are + 动词-ing。"
                    "常见时间状语：now, right now, at the moment, Look!, Listen!。"
                    "特殊用法：① 表近期计划好的将来（I am leaving tomorrow.）；"
                    "② 与 always 连用表反复动作带感情色彩（He is always complaining.）。"
                    "动词 -ing 形式：一般加 -ing；e 尾去 e（make → making）；重读闭音节双写末字母（run → running）。"
                ),
                "examples": [
                    {"en": "Listen! Someone is knocking at the door.", "zh": "听！有人在敲门。"},
                    {"en": "We are having dinner now.", "zh": "我们现在正在吃晚饭。"},
                    {"en": "I am flying to Shanghai tomorrow.", "zh": "我明天飞往上海。（已安排好的将来）"},
                ],
                "points": [
                    "结构：am/is/are + doing",
                    "表示此刻或现阶段正在进行的动作",
                    "常与 now, Look!, Listen!, at the moment 连用",
                    "come, go, leave, arrive 等移位动词可用进行时表将来",
                ],
                "mistakes": [
                    "❌ He is sleep now.（漏加 -ing，应为 sleeping）",
                    "❌ I am knowing the answer.（know 是状态动词，不用进行时）",
                ],
                "quiz": [
                    {
                        "q": "Be quiet! The baby ___ in the next room.",
                        "options": ["sleep", "is sleeping", "sleeps", "slept"],
                        "answer": 1,
                        "tip": "Be quiet! 提示此刻正在发生，用现在进行时 is sleeping。"
                    },
                    {
                        "q": "They ___ a meeting at the moment.",
                        "options": ["have", "are having", "had", "has"],
                        "answer": 1,
                        "tip": "at the moment 是现在进行时标志，用 are having。"
                    },
                ],
            },
            {
                "id": "tense-past-continuous",
                "title": "过去进行时",
                "summary": "was/were + doing，表过去某时刻正在进行的动作",
                "explanation": (
                    "过去进行时表示过去某一时刻或某段时间内正在进行的动作。"
                    "结构：主语 + was/were + 动词-ing（I/he/she/it 用 was，you/we/they 用 were）。"
                    "常见时间状语：at that time, at eight last night, this time yesterday。"
                    "典型句型：① was/were doing ... when ... did ...（正在做某事，这时突然……）；"
                    "② while ... was doing, ... did ...（在……期间，另一件事发生了）。"
                ),
                "examples": [
                    {"en": "I was watching TV at eight last night.", "zh": "昨晚八点我正在看电视。"},
                    {"en": "She was reading when the lights went out.", "zh": "她正在读书，这时灯灭了。"},
                    {"en": "While they were playing, it began to snow.", "zh": "他们正在玩的时候，开始下雪了。"},
                ],
                "points": [
                    "结构：was/were + doing",
                    "表过去某时刻/时段正在进行的动作",
                    "常与 when 突然性动作或 while 持续性动作搭配",
                    "过去进行时与一般过去时区别：前者是背景，后者是事件",
                ],
                "mistakes": [
                    "❌ I was watch TV at that time.（漏加 -ing，应为 watching）",
                    "❌ They was playing basketball.（复数主语要用 were）",
                ],
                "quiz": [
                    {
                        "q": "What ___ you ___ at seven yesterday evening?",
                        "options": ["was, doing", "were, doing", "are, doing", "did, do"],
                        "answer": 1,
                        "tip": "主语 you 配 were，过去进行时结构 were + doing。"
                    },
                    {
                        "q": "While I ___ in the street, I met an old friend.",
                        "options": ["walk", "was walking", "am walking", "have walked"],
                        "answer": 1,
                        "tip": "while 引导持续性动作，用过去进行时 was walking。"
                    },
                ],
            },
            {
                "id": "tense-future-continuous",
                "title": "将来进行时",
                "summary": "will be + doing，表将来某时刻将正在进行的动作",
                "explanation": (
                    "将来进行时表示将来某一时刻正在进行的动作，或按计划将来一定会发生的事。"
                    "结构：主语 + will be + 动词-ing。"
                    "常见时间状语：this time tomorrow, at eight next Monday, at this time next week。"
                    "它也常用来委婉询问对方计划（Will you be using the car tomorrow?）。"
                ),
                "examples": [
                    {"en": "This time tomorrow I will be flying to Beijing.", "zh": "明天这个时候我将正在飞往北京的途中。"},
                    {"en": "They will be having a meeting at three o'clock.", "zh": "三点钟他们将正在开会。"},
                    {"en": "Will you be using your bike this afternoon?", "zh": "今天下午你会用你的自行车吗？（委婉询问）"},
                ],
                "points": [
                    "结构：will be + doing",
                    "表将来某时刻正在进行的动作",
                    "常与 this time tomorrow, at eight next Monday 等连用",
                    "可用于礼貌地询问别人的计划",
                ],
                "mistakes": [
                    "❌ I will do my homework this time tomorrow.（应强调那时正在做：will be doing）",
                    "❌ She will be is sleeping.（be 后接 -ing，不能再用 is）",
                ],
                "quiz": [
                    {
                        "q": "This time next week we ___ on the beach.",
                        "options": ["will lie", "will be lying", "lie", "are lying"],
                        "answer": 1,
                        "tip": "this time next week 提示将来某时刻正在做，用 will be lying。"
                    },
                    {
                        "q": "At eight tomorrow morning she ___ to work.",
                        "options": ["will drive", "will be driving", "drives", "drove"],
                        "answer": 1,
                        "tip": "明天早上八点那个时刻将正在开车，用将来进行时。"
                    },
                ],
            },
            {
                "id": "tense-present-perfect",
                "title": "现在完成时",
                "summary": "have/has + 过去分词，表过去动作对现在的影响、经历或持续",
                "explanation": (
                    "现在完成时的核心是“过去做了，现在有结果或影响”。三大用法："
                    "① 动作已完成但对现在有影响（I have lost my key. 现在没有钥匙）；"
                    "② 经历，表示曾经做过（have been to / have ever done）；"
                    "③ 从过去持续到现在（常与 for, since 连用，也可延续到将来）。"
                    "结构：主语 + have/has + 过去分词。"
                    "标志词：already（已）, yet（还，用于否定疑问）, just（刚刚）, ever（曾经）, never（从不）, for + 时段, since + 时间点。"
                    "注意 have been to（去过，已回）与 have gone to（去了，未回）的区别。"
                ),
                "examples": [
                    {"en": "I have finished my homework.", "zh": "我已经做完作业了。（对现在的影响：现在可以玩了）"},
                    {"en": "She has been to Paris twice.", "zh": "她去过巴黎两次。（经历）"},
                    {"en": "We have lived here for ten years.", "zh": "我们在这里住了十年了。（持续到现在）"},
                ],
                "points": [
                    "结构：have/has + 过去分词（各人称都用 have/has + done）",
                    "不与明确的过去时间状语连用（yesterday, last year, in 2020）",
                    "for + 时间段（for three years），since + 时间点（since 2020）",
                    "have been to 表去过已回；have gone to 表去了未回",
                ],
                "mistakes": [
                    "❌ I have seen this film yesterday.（完成时不能与 yesterday 连用，应改为 saw）",
                    "❌ She has went to the shop.（过去分词用 gone，不是 went）",
                ],
                "quiz": [
                    {
                        "q": "He ___ in this company since 2018.",
                        "options": ["works", "worked", "has worked", "is working"],
                        "answer": 2,
                        "tip": "since 2018 表示从过去持续到现在，用现在完成时 has worked。"
                    },
                    {
                        "q": "—Where is Tom? —He ___ to the library.",
                        "options": ["has been", "has gone", "went", "goes"],
                        "answer": 1,
                        "tip": "汤姆不在，说明他去了图书馆还没回来，用 has gone to。"
                    },
                ],
            },
            {
                "id": "tense-past-perfect",
                "title": "过去完成时",
                "summary": "had + 过去分词，表“过去的过去”",
                "explanation": (
                    "过去完成时表示在过去某一时间或动作之前已经完成的动作，即“过去的过去”。"
                    "结构：主语 + had + 过去分词。"
                    "典型用法：① 与 by the time, before, after 引导的过去时间连用；"
                    "② 在宾语从句中（He said he had finished it.）；"
                    "③ 与过去完成时连用的句型：Hardly had ... when ... / No sooner had ... than ...。"
                ),
                "examples": [
                    {"en": "By the time I got there, the film had already begun.", "zh": "我到那儿时，电影已经开始了。"},
                    {"en": "She told me she had seen the film before.", "zh": "她告诉我她以前看过那部电影。"},
                    {"en": "Hardly had he sat down when the phone rang.", "zh": "他刚坐下，电话就响了。"},
                ],
                "points": [
                    "结构：had + 过去分词",
                    "表示在过去某个时间点之前已完成的动作",
                    "常与 by the end of last term, before 等过去时间连用",
                    "句中通常会有一个过去的动作作参照点",
                ],
                "mistakes": [
                    "❌ By the time he arrived, she already left.（left 发生在 arrived 之前，应用 had left）",
                    "❌ He said he has finished it.（主句是 said，从句表示过去的过去，用 had finished）",
                ],
                "quiz": [
                    {
                        "q": "When I arrived at the station, the train ___ already left.",
                        "options": ["has", "had", "have", "was"],
                        "answer": 1,
                        "tip": "火车离开发生在我到达之前，是“过去的过去”，用 had left。"
                    },
                    {
                        "q": "She said she ___ never been to China before.",
                        "options": ["has", "had", "have", "was"],
                        "answer": 1,
                        "tip": "主句 said 是过去时，“去过某地”在此之前发生，用 had been。"
                    },
                ],
            },
            {
                "id": "tense-future-perfect",
                "title": "将来完成时",
                "summary": "will have + 过去分词，表到将来某时已完成",
                "explanation": (
                    "将来完成时表示到将来某一时间为止已经完成或做出的动作。"
                    "结构：主语 + will have + 过去分词。"
                    "常见时间状语：by the end of next month, by the time you come back, by then。"
                    "它常与 by 引导的时间状语连用，也可用于表示对将来的推测"
                    "（You will have heard of it. 你多半已经听说了）。"
                ),
                "examples": [
                    {"en": "By the end of this month, I will have finished the book.", "zh": "到本月底我将已经读完这本书。"},
                    {"en": "They will have arrived by six o'clock.", "zh": "到六点钟他们将已经到达。"},
                    {"en": "You will have heard of the news.", "zh": "你多半已经听说这消息了。（对现在的推测）"},
                ],
                "points": [
                    "结构：will have + 过去分词",
                    "表示到将来某个时间点已经完成的动作",
                    "常与 by the end of, by the time, before 等连用",
                    "也可用于对现在情况的推测",
                ],
                "mistakes": [
                    "❌ By next year I will finish college.（强调到那时已完成，应用 will have finished）",
                    "❌ She will have went home.（过去分词是 gone，不是 went）",
                ],
                "quiz": [
                    {
                        "q": "By the time you get back, I ___ the house.",
                        "options": ["will clean", "will have cleaned", "clean", "cleaned"],
                        "answer": 1,
                        "tip": "到你回来时已经打扫完，是到将来完成的动作，用 will have cleaned。"
                    },
                    {
                        "q": "By next summer they ___ here for ten years.",
                        "options": ["will live", "will have lived", "live", "lived"],
                        "answer": 1,
                        "tip": "到将来某时已持续十年，用将来完成时 will have lived。"
                    },
                ],
            },
            {
                "id": "tense-present-perfect-continuous",
                "title": "现在完成进行时",
                "summary": "have/has been + doing，表从过去持续到现在并可能继续",
                "explanation": (
                    "现在完成进行时表示从过去某时开始一直持续到现在的动作，强调持续性，可能仍将继续。"
                    "结构：主语 + have/has been + 动词-ing。"
                    "常与 for, since, all day, these days 等连用。"
                    "与现在完成时的区别：完成时强调“已完成/有结果”，完成进行时强调“一直在做、可能未完成”"
                    "（I have read the book. 读完了 vs I have been reading the book. 一直在读）。"
                ),
                "examples": [
                    {"en": "I have been waiting for two hours.", "zh": "我已经等了两个小时了。（可能还在等）"},
                    {"en": "She has been working on the project since Monday.", "zh": "她从周一开始一直在做这个项目。"},
                    {"en": "It has been raining all day.", "zh": "雨下了一整天了。"},
                ],
                "points": [
                    "结构：have/has been + doing",
                    "强调动作从过去持续到现在，可能仍将继续",
                    "常与 for, since, all day, all morning 连用",
                    "与现在完成时区别：完成时重结果，完成进行时重过程",
                ],
                "mistakes": [
                    "❌ I have been waited for an hour.（been 后接 -ing，应为 waiting）",
                    "❌ She has been know him for years.（know 是状态动词，用现在完成时 has known）",
                ],
                "quiz": [
                    {
                        "q": "They ___ for the bus for half an hour.",
                        "options": ["have waited", "have been waiting", "wait", "are waiting"],
                        "answer": 1,
                        "tip": "强调从过去持续到现在还在等的动作，用 have been waiting。"
                    },
                    {
                        "q": "Look at her eyes. She ___ .",
                        "options": ["has cried", "has been crying", "cries", "cried"],
                        "answer": 1,
                        "tip": "眼睛红是持续哭的结果迹象，强调刚哭过且可能还在哭，用 has been crying。"
                    },
                ],
            },
            {
                "id": "tense-past-perfect-continuous",
                "title": "过去完成进行时",
                "summary": "had been + doing，表到过去某时为止一直持续的动作",
                "explanation": (
                    "过去完成进行时表示到过去某一时间为止一直在持续的动作，强调持续性和量。"
                    "结构：主语 + had been + 动词-ing。"
                    "常见时间状语：for two hours, since morning, before 等。"
                    "它常解释过去某个状态的原因（He was tired because he had been working all day.）。"
                ),
                "examples": [
                    {"en": "He was tired because he had been working all day.", "zh": "他很累，因为他干了一整天活。"},
                    {"en": "They had been waiting for two hours before the train came.", "zh": "火车来之前他们已经等了两个小时。"},
                    {"en": "She had been living there since 2010.", "zh": "她从 2010 年起就一直住在那里。"},
                ],
                "points": [
                    "结构：had been + doing",
                    "表示到过去某时为止一直在持续的动作",
                    "常与 for + 时段、since + 时间点连用",
                    "常用于解释过去某种状态的原因",
                ],
                "mistakes": [
                    "❌ He was tired because he has been working all day.（主句是 was，从句用 had been working）",
                    "❌ They had been wait for hours.（been 后接 -ing，应为 waiting）",
                ],
                "quiz": [
                    {
                        "q": "She was exhausted because she ___ all night.",
                        "options": ["has studied", "had been studying", "studied", "was studying"],
                        "answer": 1,
                        "tip": "熬夜学习发生在 was exhausted 之前并持续整晚，用过去完成进行时。"
                    },
                    {
                        "q": "By the time we arrived, they ___ for an hour.",
                        "options": ["had waited", "had been waiting", "have waited", "waited"],
                        "answer": 1,
                        "tip": "在我们到达前已持续等了一小时，强调持续性，用 had been waiting。"
                    },
                ],
            },
        ],
    },
]
