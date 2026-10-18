# ---------- 前端构建 ----------
# 国内网络拉不动 Docker Hub / npm 官方源时, 可通过环境变量换镜像源
#   DOCKERHUB_MIRROR  基础镜像源   (默认 docker.m.daocloud.io)
#   NPM_REGISTRY      npm 源      (默认 https://registry.npmmirror.com)
ARG DOCKERHUB_MIRROR=docker.m.daocloud.io
ARG NPM_REGISTRY=https://registry.npmmirror.com
FROM ${DOCKERHUB_MIRROR}/node:22-alpine AS frontend
ARG NPM_REGISTRY
# 生产构建隐藏的板块（逗号分隔：nav,grammar）；留空则全部显示
ARG VITE_HIDDEN_SECTIONS=""
ENV VITE_HIDDEN_SECTIONS=$VITE_HIDDEN_SECTIONS
WORKDIR /build
RUN npm config set registry "$NPM_REGISTRY"
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci --no-fund --no-audit
COPY frontend/ ./
RUN npm run build

# ---------- 后端运行 ----------
FROM ${DOCKERHUB_MIRROR}/python:3.12-slim
WORKDIR /app
ENV FRONTEND_DIST=/app/frontend/dist
ENV DATA_DIR=/app/data

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/app ./app
COPY --from=frontend /build/dist ./frontend/dist

EXPOSE 8000
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
