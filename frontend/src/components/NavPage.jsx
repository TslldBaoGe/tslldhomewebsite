import { useCallback, useEffect, useState } from 'react'
import { fetchNav, navApi, adminToken } from '../api.js'

export default function NavPage() {
  const [data, setData] = useState(null)
  const [loadErr, setLoadErr] = useState('')
  const [authed, setAuthed] = useState(() => adminToken.get() !== '')
  const [showPw, setShowPw] = useState(false)
  const [pw, setPw] = useState('')
  const [pwErr, setPwErr] = useState('')
  const [editing, setEditing] = useState(false)
  const [busy, setBusy] = useState(false)

  const load = useCallback(async () => {
    setLoadErr('')
    try {
      setData(await fetchNav())
    } catch {
      setLoadErr('导航数据加载失败，请确认后端服务已启动')
    }
  }, [])

  useEffect(() => {
    load()
  }, [load])

  // 所有管理操作的统一入口：拿到接口返回的最新数据直接刷新视图
  const run = useCallback(
    async (fn) => {
      setBusy(true)
      try {
        setData(await fn())
        setPwErr('')
      } catch (err) {
        if (err.unauthorized) {
          adminToken.clear()
          setAuthed(false)
          setEditing(false)
          setShowPw(true)
          setPwErr('登录已失效，请重新输入管理密码')
        } else {
          setPwErr(err.message)
        }
      } finally {
        setBusy(false)
      }
    },
    [],
  )

  async function doAuth(e) {
    e.preventDefault()
    setBusy(true)
    setPwErr('')
    try {
      await navApi.auth(pw)
      adminToken.set(pw)
      setAuthed(true)
      setEditing(true)
      setShowPw(false)
      setPw('')
    } catch (err) {
      setPwErr(err.unauthorized ? '管理密码错误' : err.message)
    } finally {
      setBusy(false)
    }
  }

  function doLogout() {
    adminToken.clear()
    setAuthed(false)
    setEditing(false)
  }

  const categories = data?.categories ?? []

  return (
    <section className="navpage" aria-label="导航板块">
      <div className="nav-top">
        <h2 className="nav-title">
          书签导航 <em>NAV</em>
        </h2>
        <div className="nav-admin">
          {!authed && !showPw && (
            <button className="mini-btn" onClick={() => setShowPw(true)}>
              管理
            </button>
          )}
          {!authed && showPw && (
            <form className="pw-form" onSubmit={doAuth}>
              <input
                type="password"
                placeholder="管理密码"
                value={pw}
                autoFocus
                onChange={(e) => setPw(e.target.value)}
              />
              <button className="mini-btn" disabled={busy || !pw}>
                确认
              </button>
              <button
                type="button"
                className="mini-btn ghost"
                onClick={() => {
                  setShowPw(false)
                  setPw('')
                  setPwErr('')
                }}
              >
                取消
              </button>
              {pwErr && <span className="pw-err">{pwErr}</span>}
            </form>
          )}
          {authed && (
            <>
              <button
                className={editing ? 'mini-btn on' : 'mini-btn'}
                onClick={() => setEditing(!editing)}
              >
                {editing ? '完成编辑' : '编辑'}
              </button>
              <button className="mini-btn ghost" onClick={doLogout}>
                退出管理
              </button>
              {pwErr && <span className="pw-err">{pwErr}</span>}
            </>
          )}
        </div>
      </div>

      {editing && (
        <p className="nav-hint">编辑模式：可直接新增/重命名分类，添加、修改或删除导航，操作即时保存。</p>
      )}

      {loadErr && (
        <div className="notice error">
          <p>{loadErr}</p>
          <button onClick={load}>重试</button>
        </div>
      )}

      {!data && !loadErr && (
        <div className="nav-grid">
          {Array.from({ length: 4 }, (_, i) => (
            <div key={i} className="nav-cat skeleton" />
          ))}
        </div>
      )}

      {data && (
        <div className="nav-grid">
          {categories.map((cat) => (
            <CategoryCard key={cat.id} cat={cat} editing={editing} run={run} busy={busy} />
          ))}
          {editing && <AddCategoryForm run={run} busy={busy} />}
        </div>
      )}

      {data && categories.length === 0 && !editing && (
        <p className="nav-empty">还没有导航内容，点击右上角「管理」添加你的第一个分类。</p>
      )}
    </section>
  )
}

/* ---------------- 分类卡片 ---------------- */

function CategoryCard({ cat, editing, run, busy }) {
  const [renaming, setRenaming] = useState(false)
  const [name, setName] = useState(cat.name)
  const [adding, setAdding] = useState(false)

  function saveRename(e) {
    e.preventDefault()
    if (!name.trim() || name === cat.name) {
      setRenaming(false)
      setName(cat.name)
      return
    }
    run(() => navApi.renameCategory(cat.id, name))
    setRenaming(false)
  }

  function removeCat() {
    if (window.confirm(`删除分类「${cat.name}」及其下全部 ${cat.links.length} 个导航？`)) {
      run(() => navApi.deleteCategory(cat.id))
    }
  }

  return (
    <div className="nav-cat">
      <div className="nav-cat-head">
        {renaming ? (
          <form className="rename-form" onSubmit={saveRename}>
            <input value={name} autoFocus onChange={(e) => setName(e.target.value)} />
            <button className="mini-btn" disabled={busy}>存</button>
          </form>
        ) : (
          <>
            <h3 title={cat.name}>{cat.name}</h3>
            <span className="cat-count">{cat.links.length}</span>
            {editing && (
              <span className="cat-actions">
                <button
                  className="icon-btn"
                  title="重命名分类"
                  onClick={() => {
                    setName(cat.name)
                    setRenaming(true)
                  }}
                >
                  ✎
                </button>
                <button className="icon-btn danger" title="删除分类" onClick={removeCat}>
                  ×
                </button>
              </span>
            )}
          </>
        )}
      </div>

      <div className="nav-links">
        {cat.links.map((link) => (
          <LinkRow key={link.id} link={link} editing={editing} run={run} busy={busy} />
        ))}
        {cat.links.length === 0 && <p className="nav-cat-empty">暂无导航</p>}
      </div>

      {editing &&
        (adding ? (
          <AddLinkForm
            cat={cat}
            run={run}
            busy={busy}
            onDone={() => setAdding(false)}
          />
        ) : (
          <button className="add-link-btn" onClick={() => setAdding(true)}>
            ＋ 添加导航
          </button>
        ))}
    </div>
  )
}

/* ---------------- 单条导航 ---------------- */

function LinkRow({ link, editing, run, busy }) {
  const [edit, setEdit] = useState(false)
  const [name, setName] = useState(link.name)
  const [url, setUrl] = useState(link.url)

  function save(e) {
    e.preventDefault()
    if (!name.trim() || !url.trim()) return
    run(() => navApi.updateLink(link.id, name, url))
    setEdit(false)
  }

  function remove() {
    if (window.confirm(`删除导航「${link.name}」？`)) {
      run(() => navApi.deleteLink(link.id))
    }
  }

  if (edit) {
    return (
      <form className="link-edit" onSubmit={save}>
        <input value={name} autoFocus onChange={(e) => setName(e.target.value)} placeholder="名称" />
        <input value={url} onChange={(e) => setUrl(e.target.value)} placeholder="网址" />
        <div className="link-edit-btns">
          <button className="mini-btn" disabled={busy}>保存</button>
          <button type="button" className="mini-btn ghost" onClick={() => setEdit(false)}>
            取消
          </button>
        </div>
      </form>
    )
  }

  return (
    <div className="nav-link">
      <span className={`avatar av-${(link.name.charCodeAt(0) || 0) % 4}`}>
        {(link.name.trim()[0] || '?').toUpperCase()}
      </span>
      <a className="name" href={link.url} target="_blank" rel="noreferrer" title={link.url}>
        {link.name}
      </a>
      {editing && (
        <span className="link-actions">
          <button
            className="icon-btn"
            title="编辑"
            onClick={() => {
              setName(link.name)
              setUrl(link.url)
              setEdit(true)
            }}
          >
            ✎
          </button>
          <button className="icon-btn danger" title="删除" onClick={remove}>
            ×
          </button>
        </span>
      )}
    </div>
  )
}

/* ---------------- 表单 ---------------- */

function AddLinkForm({ cat, run, busy, onDone }) {
  const [name, setName] = useState('')
  const [url, setUrl] = useState('')

  function save(e) {
    e.preventDefault()
    if (!name.trim() || !url.trim()) return
    run(async () => {
      const data = await navApi.addLink(cat.id, name, url)
      onDone()
      return data
    })
  }

  return (
    <form className="add-link-form" onSubmit={save}>
      <input value={name} autoFocus onChange={(e) => setName(e.target.value)} placeholder="名称" />
      <input value={url} onChange={(e) => setUrl(e.target.value)} placeholder="网址，如 github.com" />
      <div className="link-edit-btns">
        <button className="mini-btn" disabled={busy || !name.trim() || !url.trim()}>添加</button>
        <button type="button" className="mini-btn ghost" onClick={onDone}>收起</button>
      </div>
    </form>
  )
}

function AddCategoryForm({ run, busy }) {
  const [name, setName] = useState('')
  const [open, setOpen] = useState(false)

  function save(e) {
    e.preventDefault()
    if (!name.trim()) return
    run(async () => {
      const data = await navApi.addCategory(name)
      setName('')
      setOpen(false)
      return data
    })
  }

  if (!open) {
    return (
      <button className="nav-cat add-cat" onClick={() => setOpen(true)}>
        ＋ 新建分类
      </button>
    )
  }
  return (
    <form className="nav-cat add-cat open" onSubmit={save}>
      <input
        value={name}
        autoFocus
        onChange={(e) => setName(e.target.value)}
        placeholder="分类名称"
      />
      <div className="link-edit-btns">
        <button className="mini-btn" disabled={busy || !name.trim()}>创建</button>
        <button type="button" className="mini-btn ghost" onClick={() => setOpen(false)}>
          取消
        </button>
      </div>
    </form>
  )
}
