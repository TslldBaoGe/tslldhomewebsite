import { useCallback, useEffect, useState } from 'react'
import { fetchNews, REFRESH_SECONDS } from './api.js'
import Masthead from './components/Masthead.jsx'
import Hotboard from './components/Hotboard.jsx'

export default function App() {
  const [platform, setPlatform] = useState('zhihu')
  const [boards, setBoards] = useState(null)
  const [updatedAt, setUpdatedAt] = useState(null)
  const [errors, setErrors] = useState({})
  const [loading, setLoading] = useState(true)
  const [refreshing, setRefreshing] = useState(false)
  const [secondsLeft, setSecondsLeft] = useState(REFRESH_SECONDS)

  const load = useCallback(async (force = false) => {
    if (force) setRefreshing(true)
    try {
      const res = await fetchNews(force)
      setBoards(res.data ?? {})
      setUpdatedAt(res.updated_at ?? null)
      setErrors(res.errors ?? {})
    } catch (err) {
      setErrors({ _global: `无法连接后端服务（${err.message}），请确认 backend/start.bat 已启动` })
    } finally {
      setLoading(false)
      setRefreshing(false)
      setSecondsLeft(REFRESH_SECONDS)
    }
  }, [])

  useEffect(() => {
    load(false)
  }, [load])

  useEffect(() => {
    const timer = setInterval(() => {
      setSecondsLeft((s) => {
        if (s <= 1) {
          load(true)
          return REFRESH_SECONDS
        }
        return s - 1
      })
    }, 1000)
    return () => clearInterval(timer)
  }, [load])

  return (
    <div className={refreshing ? 'page refreshing' : 'page'}>
      <Masthead
        updatedAt={updatedAt}
        secondsLeft={secondsLeft}
        refreshing={refreshing}
        onRefresh={() => load(true)}
      />
      <main className="main">
        {errors._global && (
          <div className="notice error">
            <p>{errors._global}</p>
            <button onClick={() => load(true)}>重试</button>
          </div>
        )}
        <Hotboard
          boards={boards}
          platform={platform}
          onPlatform={setPlatform}
          loading={loading}
          errors={errors}
          refreshing={refreshing}
          onRefresh={() => load(true)}
        />
      </main>
      <footer className="footer">
        <p>数据来源：知乎热榜 · AI资讯 · 央视新闻 · 微博热搜 · 抖音热搜 · B站热搜，每 5 分钟自动更新</p>
      </footer>
    </div>
  )
}
