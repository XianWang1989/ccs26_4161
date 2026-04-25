
from gluon import DAL, Cache

# Set up database connection with pooling
db = DAL('mysql://username:password@localhost/dbname', pool_size=10)
cache = Cache('ram')

def get_query_data(query):
    # Use caching to store results for 60 seconds
    return cache.ram('query_cache_key', lambda: db.executesql(query, as_dict=True), time_expire=60)

# Example query
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration', ...
    FROM ... AS ris
    JOIN ... AS sd ON ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
    AND ris.... >= '2010-8-15'
    AND ris.... <= '2014-8-22'
"""

# Call the function
raw_data = get_query_data(query)
