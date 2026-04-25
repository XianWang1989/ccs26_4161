
import logging
from gluon import cache

logging.basicConfig(level=logging.DEBUG)

def get_data():
    query = """SELECT ..."""  # Your SQL query here

    # Check cache first
    cache_key = 'my_query_cache'
    raw_data = cache.ram(cache_key, lambda: dbs.executesql(query, as_dict=True), time_expiry=300)

    # Log execution time
    if raw_data:
        logging.debug(f"Query executed and cached: {cache_key}")
    else:
        logging.error(f"Failed to execute query: {query}")

    return raw_data
