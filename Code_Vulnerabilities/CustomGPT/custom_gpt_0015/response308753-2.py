
cache_time = 60  # Cache for 1 minute
cached_data = cache.ram('key_name', lambda: db.executesql(query, as_dict=True), cache_time)
