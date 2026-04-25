
# Example of caching the result
cache_data = cache.ram('some_unique_key', lambda: db.executesql(query, as_dict=True), time_expire=60)
