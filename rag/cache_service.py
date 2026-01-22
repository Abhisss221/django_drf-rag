import hashlib
import time


class CacheService:
    def __init__(self):
        self._cache = {}

    def _hash_question(self, question: str) -> str:
        return hashlib.sha256(question.encode()).hexdigest()[:8]

    def make_key(self, user_id: int, question: str, data_version: int):
        q_hash = self._hash_question(question)
        return f"rag:{user_id}:{q_hash}:{data_version}"

    def get(self, key: str):
        entry = self._cache.get(key)
        if not entry:
            return None

        value, timestamp = entry
        return value

    def set(self, key: str, value: str):
        self._cache[key] = (value, time.time())

    def invalidate_user(self, user_id: int):
        keys_to_delete = [
            k for k in self._cache if k.startswith(f"rag:{user_id}:")
        ]
        for k in keys_to_delete:
            del self._cache[k]


cache_service = CacheService()
