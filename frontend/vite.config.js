import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// 开发模式下把 /api 代理到 FastAPI 后端（backend/start.bat 默认跑在 8001）
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/api': 'http://127.0.0.1:8001',
    },
  },
})
