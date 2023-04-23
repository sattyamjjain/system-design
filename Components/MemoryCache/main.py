import time


class MemoryCache:
    def __init__(self, capacity=1000, default_ttl=60):
        self.cache = {}
        self.capacity = capacity
        self.default_ttl = default_ttl

    def get(self, key):
        if key not in self.cache:
            return None

        value, expiration = self.cache[key]
        if expiration is not None and expiration < time.time():
            del self.cache[key]
            return None

        return value

    def set(self, key, value, ttl=None):
        if len(self.cache) >= self.capacity:
            self.evict()

        if ttl is None:
            ttl = self.default_ttl

        expiration = time.time() + ttl
        self.cache[key] = (value, expiration)

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]

    def evict(self):
        now = time.time()
        expired_keys = [k for k, (v, e) in self.cache.items() if e is not None and e < now]
        for key in expired_keys:
            del self.cache[key]

    def clear(self):
        self.cache.clear()
