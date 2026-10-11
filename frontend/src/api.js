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
