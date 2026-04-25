
from gluon import cache

# Caching example
def cached_query(dbs, query):
    cache_key = f"query_cache:{query}"
    return cache.cache_routing.get(cache_key) or cache.ram(cache_key, expires=60, lambda: dbs.executesql(query, as_dict=True))
