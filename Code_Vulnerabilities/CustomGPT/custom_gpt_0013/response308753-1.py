
import time

# Start the timer
start_time = time.time()

# Caching the query results
query = "SELECT * FROM your_table WHERE conditions"
cache_key = 'your_cache_key'

# Try to retrieve from cache first
cached_result = db.cache.ram(cache_key, lambda: db.executesql(query, as_dict=True), time_expire=300)

# If cache hit, print from cache, otherwise execute and cache result
if cached_result:
    print("Using cached result.")
    raw_data = cached_result
else:
    print("Query executed and cached.")
    raw_data = db.executesql(query, as_dict=True)

# Measure elapsed time
elapsed_time = time.time() - start_time
print(f"Query execution time: {elapsed_time:.4f} seconds")
