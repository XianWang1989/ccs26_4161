
# Use the caching mechanisms provided by web2py
cache_query = cache.ram('my_query_cache_key', lambda: db.executesql(query, as_dict=True), time_expire=60)
