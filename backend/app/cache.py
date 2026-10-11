import asyncio
import time


class TTLCache:
    """Tiny per-key TTL cache that also collapses concurrent identical fetches."""

    def __init__(self, ttl_seconds: float):
        self.ttl = ttl_seconds
        self._data: dict = {}
        self._expires: dict = {}
        self._lock = asyncio.Lock()

    async def put(self, key: str, value):
        async with self._lock:
            self._data[key] = value
            self._expires[key] = time.monotonic() + self.ttl

    async def get_or_set(self, key: str, factory):
        async with self._lock:
            now = time.monotonic()
            if key in self._data and self._expires[key] > now:
                return self._data[key]
            value = await factory()
            self._data[key] = value
            self._expires[key] = now + self.ttl
            return value
