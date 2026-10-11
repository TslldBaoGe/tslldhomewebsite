#!/usr/bin/env bash
# 一键部署 / 更新脚本（在服务器上运行）
#
# 首次部署:  在空目录中放置本脚本后执行  WEB_PORT=8080 ./deploy.sh
# 日常更新:  再次执行同一命令即可（自动 git pull + 重建容器）
#
# 端口说明: 宿主机端口通过 WEB_PORT 指定，默认 8090，容器内部固定 8000。
set -euo pipefail

REPO_URL="https://github.com/TslldBaoGe/tslldhomewebsite.git"
WEB_PORT="${WEB_PORT:-8090}"
export WEB_PORT

command -v docker >/dev/null || { echo "错误: 未安装 docker"; exit 1; }
docker compose version >/dev/null 2>&1 || { echo "错误: 缺少 docker compose 插件"; exit 1; }

# 首次运行时克隆仓库；之后增量更新
if [ ! -d .git ]; then
  if [ -n "$(ls -A . 2>/dev/null)" ]; then
    echo "错误: 当前目录非空且不是 git 仓库，请在空目录中运行本脚本"
    exit 1
  fi
  git clone "$REPO_URL" .
fi

echo ">>> 拉取最新代码..."
git pull --ff-only

echo ">>> 构建并启动容器 (宿主机端口 ${WEB_PORT})..."
docker compose up -d --build

echo ">>> 清理无用镜像..."
docker image prune -f >/dev/null

echo
echo "✅ 部署完成: http://<服务器IP>:${WEB_PORT}"
docker compose ps
