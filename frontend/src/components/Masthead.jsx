import { useMemo } from 'react'
import { formatClock, REFRESH_SECONDS } from '../api.js'

const RING_R = 7
const RING_C = 2 * Math.PI * RING_R

export default function Masthead({ updatedAt, secondsLeft, refreshing, onRefresh }) {
  const dateStr = useMemo(() => {
    const d = new Date()
    const date = d.toLocaleDateString('zh-CN', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    })
    const week = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'][d.getDay()]
    return `${date} ${week}`
  }, [])

  const mmss = `${String(Math.floor(secondsLeft / 60)).padStart(2, '0')}:${String(
    secondsLeft % 60,
  ).padStart(2, '0')}`

  return (
    <header className="masthead">
      <div className="mast-inner">
        <div className="brand">
          <span className="seal" aria-hidden="true">
            热
          </span>
          <div className="brand-text">
            <h1>TSLL 热榜</h1>
            <p className="kicker">PERSONAL NEWSDESK · 新闻板块</p>
          </div>
        </div>

        <div className="meta">
          <p className="date">{dateStr}</p>
          <div className="status">
            {updatedAt && <span className="updated">更新于 {formatClock(updatedAt)}</span>}
            <span
              className="ring"
              title={`每 ${Math.round(REFRESH_SECONDS / 60)} 分钟自动刷新`}
            >
              <svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true">
                <circle cx="10" cy="10" r={RING_R} className="ring-track" />
                <circle
                  cx="10"
                  cy="10"
                  r={RING_R}
                  className="ring-progress"
                  strokeDasharray={RING_C}
                  strokeDashoffset={RING_C * (1 - secondsLeft / REFRESH_SECONDS)}
                />
              </svg>
              <em>{mmss}</em>
            </span>
            <button className="refresh" onClick={onRefresh} disabled={refreshing}>
              <svg viewBox="0 0 16 16" width="13" height="13" aria-hidden="true">
                <path
                  d="M13.5 8a5.5 5.5 0 1 1-1.6-3.9M13.5 1.5v3h-3"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="1.6"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              </svg>
              手动刷新
            </button>
          </div>
        </div>
      </div>
    </header>
  )
}
