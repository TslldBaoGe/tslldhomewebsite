import { formatHot } from '../api.js'

const PLATFORMS = [
  { id: 'weibo', name: '微博热搜', hue: 'weibo' },
  { id: 'douyin', name: '抖音热搜', hue: 'douyin' },
  { id: 'zhihu', name: '知乎热榜', hue: 'zhihu' },
  { id: 'bilibili', name: 'B站热搜', hue: 'bilibili' },
  { id: 'codefather', name: 'AI资讯', hue: 'codefather' },
]

const TAG_CLASS = {
  沸: 'boil',
  爆: 'boom',
  热: 'hot',
  新: 'new',
  置顶: 'top',
  娱: 'fun',
  剧: 'drama',
  综: 'variety',
  独: 'exclusive',
}

export default function Hotboard({ boards, platform, onPlatform, loading, errors, refreshing, onRefresh }) {
  const board = boards?.[platform] ?? null
  const boardError = !loading && !board ? errors[platform] ?? '抓取失败，请稍后重试' : null
  const items = board?.items ?? []
  // 没有热度数据的平台（如 AI 资讯）按资讯流样式渲染
  const isFeed = items.length > 0 && items.every((it) => !it.hot)
  const maxHot = items.reduce((m, it) => Math.max(m, it.hot ?? 0), 0) || 1

  return (
    <section className="hotboard" aria-label="热搜榜">
      <nav className="tabs" role="tablist">
        {PLATFORMS.map((p) => {
          const count = boards?.[p.id]?.items?.length
          return (
            <button
              key={p.id}
              role="tab"
              aria-selected={platform === p.id}
              className={platform === p.id ? 'tab active' : 'tab'}
              onClick={() => onPlatform(p.id)}
            >
              <i className={`dot ${p.hue}`} aria-hidden="true" />
              {p.name}
              {typeof count === 'number' && <span className="count">{count}</span>}
            </button>
          )
        })}
        <span className="tabs-rule" aria-hidden="true" />
      </nav>

      <ol className="list" key={platform}>
        {loading && <SkeletonRows />}
        {boardError && (
          <li className="notice error">
            <p>{boardError}</p>
            <button onClick={onRefresh} disabled={refreshing}>
              重试
            </button>
          </li>
        )}
        {!loading &&
          items.map((item, i) =>
            isFeed ? (
              <li key={`${item.title}-${i}`}>
                <a
                  className="row feed"
                  href={item.url}
                  target="_blank"
                  rel="noreferrer"
                  style={{ '--d': `${Math.min(i, 20) * 28}ms` }}
                >
                  <span className="title">{item.title}</span>
                  {item.summary && <span className="summary">{item.summary}</span>}
                </a>
              </li>
            ) : (
              <li key={`${item.title}-${i}`}>
                <a
                  className="row"
                  href={item.url}
                  target="_blank"
                  rel="noreferrer"
                  style={{
                    '--d': `${Math.min(i, 20) * 28}ms`,
                    '--heat': `${Math.max(2, Math.round(((item.hot ?? 0) / maxHot) * 100))}%`,
                  }}
                >
                  <span className={`rank ${rankClass(i)}`}>{String(i + 1).padStart(2, '0')}</span>
                  <span className="title">{item.title}</span>
                  {item.tag && (
                    <span className={`tag t-${TAG_CLASS[item.tag] ?? 'plain'}`}>{item.tag}</span>
                  )}
                  <span className="hotnum">{formatHot(item.hot)}</span>
                  <i className="heatbar" aria-hidden="true" />
                </a>
              </li>
            ),
          )}
      </ol>
    </section>
  )
}

function rankClass(i) {
  if (i === 0) return 'r1'
  if (i === 1) return 'r2'
  if (i === 2) return 'r3'
  return ''
}

function SkeletonRows() {
  return (
    <>
      {Array.from({ length: 12 }, (_, i) => (
        <li key={i} aria-hidden="true">
          <div className="row skeleton" style={{ '--d': `${i * 30}ms` }}>
            <span className="rank">&nbsp;</span>
            <span className="title">&nbsp;</span>
            <span className="hotnum">&nbsp;</span>
            <i className="heatbar" />
          </div>
        </li>
      ))}
    </>
  )
}
