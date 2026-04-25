
cache_data = cache.ram('cache_key', lambda: db.executesql(query, as_dict=True), time_expire=60)
