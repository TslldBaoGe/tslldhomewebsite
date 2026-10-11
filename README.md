# TSLL 热榜

个人综合网站：**新闻板块**（微博、抖音、知乎、B站热搜 + 鱼皮AI导航 AI 资讯，每 5 分钟自动更新）
+ **导航板块**（可自主管理的书签导航，支持分类）。

技术栈：React 19 + Vite（前端）/ Python FastAPI（后端）

## 目录结构

```
tslldwebsite/
├── backend/               FastAPI 后端
│   ├── app/
│   │   ├── main.py        路由：/api/news、/api/news/{platform}、/api/health
│   │   ├── cache.py       进程内 TTL 缓存（5 分钟）
│   │   └── sources/       微博 / 抖音 抓取适配器
│   ├── requirements.txt
│   └── start.bat          一键启动后端（127.0.0.1:8001）
└── frontend/              React 前端
    ├── src/
    │   ├── App.jsx        轮询、倒计时、状态管理
    │   ├── components/    Masthead（报头）/ Hotboard（榜单）
    │   └── styles.css     「编辑部夜班」主题
    └── start.bat          一键启动前端（127.0.0.1:5173）
```

## 导航板块

页面右上角「管理」输入管理密码（环境变量 `ADMIN_PASSWORD`，**部署前务必改掉默认值**）即可进入编辑模式：
新建/重命名/删除分类，添加、修改、删除导航，操作即时保存；保存后的数据在服务端，**任何设备访问看到的都是同一份**。

两种批量导入方式（结果一致，按需选用）：

1. **网页上导入**：编辑模式下方的「从本地文件夹导入」面板，输入文件夹路径（或书签 HTML 文件路径），
   选「合并现有」或「覆盖全部」，点「保存」。注意路径是后端所在机器的路径：本地开发填本机路径；
   服务器上填服务器路径（Docker 部署需把文件夹挂载进容器，见 compose 注释）。
2. **命令行导入**：解析结果写入 `app/seed_nav.json` 随镜像发布：

```bash
cd backend
.venv\Scripts\python scripts\import_nav_folder.py <文件夹或书签HTML路径>
```

数据文件在 `data/nav.json`（Docker 中挂载为卷，重建容器不丢）。

## 服务器部署（Docker，推荐）

一个容器搞定前后端：前端构建产物由 FastAPI 直接托管，**只需暴露一个端口**。

服务器上首次部署：

```bash
mkdir tslld && cd tslld
# 把 deploy.sh 放进该目录（或直接 clone 仓库后执行）
curl -O https://raw.githubusercontent.com/TslldBaoGe/tslldhomewebsite/main/deploy.sh
WEB_PORT=8080 bash deploy.sh
```

日常更新只需再执行一次同样的命令（自动 git pull + 重建容器）。

- `WEB_PORT`：宿主机端口，默认 `8090`（服务器上已有网站占用端口时换个就行），容器内部固定 8000
- `DOCKERHUB_MIRROR` / `NPM_REGISTRY`：国内网络拉不动 Docker Hub / npm 官方源时自动走镜像源，默认 `docker.m.daocloud.io` / `registry.npmmirror.com`，可按需覆盖
- 容器带健康检查，自动重启策略 `unless-stopped`

本地也可以跑：`docker compose up -d --build`，然后访问 `http://localhost:8090`。

## 本地开发

双击两个 `start.bat`（或手动执行）：

```bat
:: 1) 后端 —— 先初始化（仅首次）
cd backend
py -3.9 -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
start.bat

:: 2) 前端 —— 先初始化（仅首次）
cd frontend
npm install
start.bat
```

打开 <http://127.0.0.1:5173> 即可。

> 注意：本机的 Miniconda 需要 `F:\Miniconda39\Library\bin` 在 PATH 里才能加载
> ssl 模块，`backend/start.bat` 已内置该修复。

## API

| 接口 | 说明 |
| --- | --- |
| `GET /api/news` | 全部平台热搜（`?refresh=1` 绕过缓存强制刷新） |
| `GET /api/news/weibo` | 微博热搜 50 条 |
| `GET /api/news/douyin` | 抖音热搜 50 条 |
| `GET /api/news/zhihu` | 知乎热榜 30 条 |
| `GET /api/news/bilibili` | B站热搜 50 条 |
| `GET /api/news/codefather` | AI 资讯（鱼皮AI导航）20 条，带摘要 |
| `GET /api/nav` | 导航板块数据（分类 + 链接） |
| `POST /api/nav/auth` | 校验管理密码 |
| `POST/PUT/DELETE /api/nav/category[...]` | 分类管理（需 `X-Admin-Token`） |
| `POST/PUT/DELETE /api/nav/link[...]` | 导航管理（需 `X-Admin-Token`） |
| `GET /api/health` | 健康检查 |

数据说明：
- 微博走 `weibo.com/ajax/side/hotSearch`（先访问首页拿 Cookie）
- 抖音走 `iesdouyin.com` 热搜榜接口
- 知乎走 `api.zhihu.com` 移动端热榜接口（无需鉴权）
- B站走 `api.bilibili.com/x/web-interface/search/square`
- AI 资讯无公开接口，解析 `ai.codefather.cn/news` 页面内嵌的 RSC 数据

后端对上游结果做 5 分钟缓存，网络抖动自动重试 3 次，避免触发风控。
新增平台：在 `backend/app/sources/` 写一个适配器（返回 `platform/name/fetched_at/items`），
注册进 `main.py` 的 `SOURCES`，再到前端 `Hotboard.jsx` 的 `PLATFORMS` 加一个 tab 即可。
