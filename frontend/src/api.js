const CACHE_SECONDS = 300 // 与后端 CACHE_TTL_SECONDS 保持一致

export async function fetchNews(refresh = false) {
  const res = await fetch(`/api/news${refresh ? '?refresh=1' : ''}`)
  if (!res.ok) {
    let detail = `${res.status}`
    try {
      const body = await res.json()
      if (body?.detail) detail = typeof body.detail === 'string' ? body.detail : JSON.stringify(body.detail)
    } catch {
      /* ignore body parse errors */
    }
    throw new Error(detail)
  }
  return res.json()
}

export function formatHot(n) {
  if (n == null || n <= 0) return ''
  if (n >= 1e8) return trim(n / 1e8) + '亿'
  if (n >= 1e4) return trim(n / 1e4) + '万'
  return String(n)
}

function trim(x) {
  const s = x.toFixed(1)
  return s.endsWith('.0') ? s.slice(0, -2) : s
}

export function formatClock(iso) {
  if (!iso) return ''
  const d = new Date(iso)
  if (Number.isNaN(d.getTime())) return ''
  return `${String(d.getHours()).padStart(2, '0')}:${String(d.getMinutes()).padStart(2, '0')}`
}

export const REFRESH_SECONDS = CACHE_SECONDS

/* ---------------- 导航板块 ---------------- */

const ADMIN_TOKEN_KEY = 'tslld_admin_token'

export const adminToken = {
  get: () => localStorage.getItem(ADMIN_TOKEN_KEY) || '',
  set: (t) => localStorage.setItem(ADMIN_TOKEN_KEY, t),
  clear: () => localStorage.removeItem(ADMIN_TOKEN_KEY),
}

async function navWrite(path, method, body) {
  const res = await fetch(path, {
    method,
    headers: {
      'Content-Type': 'application/json',
      'X-Admin-Token': adminToken.get(),
    },
    body: body ? JSON.stringify(body) : undefined,
  })
  if (res.status === 401) {
    const err = new Error('unauthorized')
    err.unauthorized = true
    throw err
  }
  if (!res.ok) {
    let detail = `HTTP ${res.status}`
    try {
      detail = (await res.json()).detail || detail
    } catch {
      /* keep default */
    }
    throw new Error(detail)
  }
  return res.json()
}

export async function fetchNav() {
  const res = await fetch('/api/nav')
  if (!res.ok) throw new Error(`HTTP ${res.status}`)
  return res.json()
}

export const navApi = {
  auth: (password) => navWrite('/api/nav/auth', 'POST', { password }),
  addCategory: (name) => navWrite('/api/nav/category', 'POST', { name }),
  renameCategory: (id, name) => navWrite(`/api/nav/category/${id}`, 'PUT', { name }),
  deleteCategory: (id) => navWrite(`/api/nav/category/${id}`, 'DELETE'),
  addLink: (categoryId, name, url) =>
    navWrite('/api/nav/link', 'POST', { category_id: categoryId, name, url }),
  updateLink: (id, name, url) => navWrite(`/api/nav/link/${id}`, 'PUT', { name, url }),
  deleteLink: (id) => navWrite(`/api/nav/link/${id}`, 'DELETE'),
}
