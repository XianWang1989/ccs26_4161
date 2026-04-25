
from gluon import current

def fetch_data():
    db = current.db
    query = "YOUR SQL QUERY HERE"

    # Use caching to store results
    cached_data = cache.ram('sql_query_cache', lambda: db.executesql(query, as_dict=True), time_expire=60)

    return cached_data
