import { useCallback, useEffect, useState } from 'react'
import { fetchNews, REFRESH_SECONDS } from './api.js'
import Masthead from './components/Masthead.jsx'
import Hotboard from './components/Hotboard.jsx'
import NavPage from './components/NavPage.jsx'
import GrammarPage from './components/GrammarPage.jsx'

export default function App() {
  const [view, setView] = useState('news') // news | nav | grammar
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
        <nav className="sections" aria-label="板块切换">
          <button
            className={view === 'news' ? 'sec active' : 'sec'}
            onClick={() => setView('news')}
          >
            新闻板块
          </button>
          <button
            className={view === 'nav' ? 'sec active' : 'sec'}
            onClick={() => setView('nav')}
          >
            导航板块
          </button>
          <button
            className={view === 'grammar' ? 'sec active' : 'sec'}
            onClick={() => setView('grammar')}
          >
            语法板块
          </button>
          <span className="sec-rule" aria-hidden="true" />
        </nav>

        {errors._global && (
          <div className="notice error">
            <p>{errors._global}</p>
            <button onClick={() => load(true)}>重试</button>
          </div>
        )}

        {view === 'nav' ? (
          <NavPage />
        ) : view === 'grammar' ? (
          <GrammarPage />
        ) : (
          <Hotboard
            boards={boards}
            platform={platform}
            onPlatform={setPlatform}
            loading={loading}
            errors={errors}
            refreshing={refreshing}
            onRefresh={() => load(true)}
          />
        )}
      </main>
      <footer className="footer">
        <p>数据来源：微博 · 抖音 · 知乎 · B站 · 鱼皮AI导航，每 {Math.round(REFRESH_SECONDS / 60)} 分钟自动更新</p>
        <p className="tech">React + FastAPI · 由 TSLL Newsdesk 驱动</p>
      </footer>
    </div>
  )
}
