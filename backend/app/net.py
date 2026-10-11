from __future__ import annotations

import asyncio

import httpx


async def with_retry(fn, attempts: int = 3, delay: float = 1.0):
    """Retry transport-level failures (DNS hiccups, timeouts, resets).

    Local networks here resolve intermittently, so a short backoff makes the
    upstream fetches far more reliable. Response-level errors are not retried.
    """
    last: Exception | None = None
    for i in range(attempts):
        try:
            return await fn()
        except httpx.TransportError as exc:
            last = exc
            if i < attempts - 1:
                await asyncio.sleep(delay * (i + 1))
    raise last
