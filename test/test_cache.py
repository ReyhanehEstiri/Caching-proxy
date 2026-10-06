from caching_proxy.cache import Cache


def test_cache_set_and_get():
    cache = Cache()

    cache.set("test", "hello")

    assert cache.get("test") == "hello"


def test_cache_miss():
    cache = Cache()

    assert cache.get("missing") is None


def test_cache_clear():
    cache = Cache()

    cache.set("test", "hello")
    cache.clear()

    assert cache.get("test") is None


def test_cache_is_empty():
    cache = Cache()

    assert cache.is_empty()

    cache.set("test", "hello")

    assert not cache.is_empty()

    cache.clear()

    assert cache.is_empty()