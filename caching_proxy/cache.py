import pickle
from pathlib import Path


CACHE_FILE = Path(".cache")


class Cache:

    def __init__(self):
        self.data = self._load()

    def _load(self):
        if not CACHE_FILE.exists():
            return {}

        with open(CACHE_FILE, "rb") as file:
            return pickle.load(file)

    def _save(self):
        with open(CACHE_FILE, "wb") as file:
            pickle.dump(self.data, file)

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value
        self._save()

    def clear(self):
        self.data = {}

        if CACHE_FILE.exists():
            CACHE_FILE.unlink()

    def is_empty(self):
        return len(self.data) == 0