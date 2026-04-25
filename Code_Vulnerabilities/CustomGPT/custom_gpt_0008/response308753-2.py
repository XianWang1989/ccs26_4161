
cache_time = 60  # Cache for 60 seconds
raw_data = cache.ram('query_key', lambda: db.executesql(query, as_dict=True), time_expire=cache_time)
