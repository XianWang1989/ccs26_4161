
# In your web2py model file (e.g., models/db.py)

from gluon import current

# Enable connection pooling
current.db = DAL('mysql://username:password@localhost/dbname', pool_size=10, migrate=False)

# Function to execute queries with caching
def execute_query_with_cache(query, params=None):
    cache_key = query + str(params)  # Simple cache key
    data = current.cache.get(cache_key)

    if data is None:
        data = current.db.executesql(query, params, as_dict=True)
        current.cache.put(cache_key, data, time_expire=60)  # Cache for 60 seconds

    return data

# Example of executing a query
def get_data():
    query = "SELECT * FROM your_table WHERE condition = %s"
    params = ('value',)

    raw_data = execute_query_with_cache(query, params)
    return raw_data
