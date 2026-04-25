
from gluon import current

# Example of using connection pooling
db = current.db

# Function to execute and cache results
def execute_and_cache(query):
    cache_key = hash(query)  # Simple hash for cache key
    cached_result = db.cache.get(cache_key)

    if cached_result is not None:
        return cached_result

    raw_data = db.executesql(query, as_dict=True)

    # Cache the result for future use
    db.cache[cache_key] = raw_data
    return raw_data

# Usage of the function
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       TIMESTAMPDIFF(...) - INTERVAL 1 HOUR,
       ris.ODATE as 'date',
       CONCAT(...) as 'service'
FROM ... AS ris
JOIN ... as sd ON ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
  AND ris.... >= '2010-8-15'
  AND ris.... <= '2014-8-22'
"""

# Execute the cached query
results = execute_and_cache(query)
