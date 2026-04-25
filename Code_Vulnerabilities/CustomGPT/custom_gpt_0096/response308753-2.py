
# Use caching for frequently accessed data
cache_time = 60  # cache for 60 seconds
cached_data = cache.ram('unique_cache_key', lambda: db.executesql(query, as_dict=True), time_expiry=cache_time)
