import { useEffect, useState } from 'react'
import { fetchGrammar } from '../api.js'

export default function GrammarPage() {
  const [grammar, setGrammar] = useState(null)
  const [loadErr, setLoadErr] = useState('')
  const [selectedCatId, setSelectedCatId] = useState(null)
  const [selectedItemId, setSelectedItemId] = useState(null)
  const [quizAnswers, setQuizAnswers] = useState({}) // { itemId: { qIdx: selectedIdx } }
  const [quizResult, setQuizResult] = useState({}) // { itemId: { qIdx: 'correct' | 'wrong' } }

  useEffect(() => {
    fetchGrammar()
      .then(setGrammar)
      .catch(() => setLoadErr('语法内容加载失败，请确认后端服务已启动'))
  }, [])

  const cats = grammar?.categories ?? []
  const cat = cats.find((c) => c.id === selectedCatId)
  const items = cat?.items ?? []
  const item = items.find((it) => it.id === selectedItemId)

  const toggleCat = (cid) => {
    setSelectedCatId((prev) => (prev === cid ? null : cid))
    setSelectedItemId(null)
  }

  const selectItem = (id) => setSelectedItemId(id)

  const handleQuiz = (itemId, qIdx, selectedIdx) => {
    const it = items.find((i) => i.id === itemId)
    if (!it) return
    const q = it.quiz[qIdx]
    const correct = q.answer === selectedIdx
    setQuizAnswers((prev) => ({
      ...prev,
      [itemId]: { ...(prev[itemId] ?? {}), [qIdx]: selectedIdx },
    }))
    setQuizResult((prev) => ({
      ...prev,
      [itemId]: { ...(prev[itemId] ?? {}), [qIdx]: correct ? 'correct' : 'wrong' },
    }))
  }

  if (loadErr) {
    return (
      <section className="grammar-page">
        <div className="notice error">
          <p>{loadErr}</p>
          <button onClick={() => window.location.reload()}>重试</button>
        </div>
      </section>
    )
  }

  if (!grammar) {
    return (
      <section className="grammar-page">
        <div className="notice error">
          <p>正在加载语法内容……</p>
        </div>
      </section>
    )
  }

  const answers = item ? (quizAnswers[item.id] ?? {}) : {}
  const results = item ? (quizResult[item.id] ?? {}) : {}

  return (
    <section className="grammar-page">
      {/* 左侧目录 */}
      <aside className="grammar-sidebar">
        {cats.map((c) => {
          const isOpen = selectedCatId === c.id
          return (
            <div className="grammar-cat" key={c.id}>
              <div
                className={`grammar-cat-title ${isOpen ? 'active' : ''}`}
                onClick={() => toggleCat(c.id)}
              >
                <span className="grammar-cat-arrow">{isOpen ? '▾' : '▸'}</span>
                {c.name} ({c.items.length})
              </div>
              {isOpen && (
                <div className="grammar-list">
                  {c.items.map((it) => (
                    <div
                      className={`grammar-item ${selectedItemId === it.id ? 'active' : ''}`}
                      key={it.id}
                      onClick={() => selectItem(it.id)}
                    >
                      <span className="grammar-item-rank">
                        {selectedItemId === it.id ? '▸' : '•'}
                      </span>
                      <span className="grammar-item-title">{it.title}</span>
                    </div>
                  ))}
                </div>
              )}
            </div>
          )
        })}
      </aside>

      {/* 右侧：欢迎页 或 详情页 */}
      <div className="grammar-detail">
        {!item ? (
          <div className="grammar-list-view">
            <h2
              style={{
                margin: '0 0 10px',
                fontFamily: 'var(--serif)',
                fontSize: '18px',
                color: 'var(--amber)',
                letterSpacing: '0.1em',
              }}
            >
              英语语法知识库
            </h2>
            <p
              style={{
                fontFamily: 'var(--fang)',
                fontSize: '13px',
                color: 'var(--paper-dim)',
                margin: '0 0 12px',
              }}
            >
              从左侧选择一个分类，再点击任意语法点查看详细解释、例句与小练习。
            </p>
          </div>
        ) : (
          <article>
            <div className="grammar-navbar">
              <button className="grammar-back" onClick={() => setSelectedItemId(null)}>
                ← 返回目录
              </button>
              <span className="grammar-bread">
                {cat?.name} &gt; {item.title}
              </span>
            </div>

            <div className="grammar-head">
              <p className="grammar-head-summary">{item.summary}</p>
              <h1 className="grammar-head-title">{item.title}</h1>
            </div>

            <section className="grammar-explain">
              <h4>详细解释</h4>
              <p>{item.explanation}</p>
              {item.examples?.length > 0 && (
                <div className="example-card">
                  {item.examples.map((ex, i) => (
                    <div className="example-item" key={i}>
                      <div className="example-label">{i % 2 === 0 ? '英文' : '中文'}</div>
                      <p className="example-text">{ex.en}</p>
                      <p className="example-text" style={{ marginTop: '6px', fontSize: '13px' }}>
                        {ex.zh}
                      </p>
                    </div>
                  ))}
                </div>
              )}
            </section>

            {item.points?.length > 0 && (
              <section className="grammar-section">
                <div className="grammar-section-head">
                  <h4>💡 要点</h4>
                </div>
                <div className="grammar-section-body">
                  <ul className="points-list">
                    {item.points.map((pt, i) => (
                      <li key={i}>{pt}</li>
                    ))}
                  </ul>
                </div>
              </section>
            )}

            {item.mistakes?.length > 0 && (
              <section className="grammar-section">
                <div className="grammar-section-head">
                  <h4>⚠️ 常见错点</h4>
                </div>
                <div className="grammar-section-body">
                  <ul className="mistakes-list">
                    {item.mistakes.map((mt, i) => (
                      <li key={i}>{mt}</li>
                    ))}
                  </ul>
                </div>
              </section>
            )}

            {item.quiz?.length > 0 && (
              <section className="grammar-quiz">
                <div className="grammar-section-head">
                  <h4>✍️ 小练习</h4>
                </div>
                <div className="grammar-section-body">
                  {item.quiz.map((q, qIdx) => {
                    const chosen = answers[qIdx]
                    const result = results[qIdx]
                    const done = result !== undefined
                    return (
                      <div className="quiz-item" key={qIdx}>
                        <p className="quiz-q">
                          {qIdx + 1}. {q.q}
                        </p>
                        <div className="quiz-options">
                          {q.options.map((opt, oIdx) => {
                            const isCorrect = q.answer === oIdx
                            const isChosen = chosen === oIdx
                            let cls = 'quiz-option'
                            if (done && isCorrect) cls += ' correct'
                            else if (done && isChosen) cls += ' wrong'
                            return (
                              <label
                                className={cls}
                                key={oIdx}
                                onClick={() => !done && handleQuiz(item.id, qIdx, oIdx)}
                              >
                                <input
                                  type="radio"
                                  name={`q-${item.id}-${qIdx}`}
                                  checked={isChosen}
                                  readOnly
                                />
                                {opt}
                              </label>
                            )
                          })}
                        </div>
                        {done && (
                          <p className={`quiz-feedback ${result}`}>
                            {result === 'correct'
                              ? '✓ 正确！'
                              : `✗ 错误，正确答案是：${q.options[q.answer]}。${q.tip}`}
                          </p>
                        )}
                      </div>
                    )
                  })}
                </div>
              </section>
            )}
          </article>
        )}
      </div>
    </section>
  )
}
