
import time
from gluon import cache

db = DAL('mysql://user:password@localhost/dbname', pool_size=10)

def run_query():
    query = "SELECT ... "  # your SQL query here

    # Timing the execution
    start_time = time.time()

    # Cached results to reduce DB load
    raw_data = cache.ram('query_cache_key', lambda: db.executesql(query, as_dict=True), timeexp=600)

    execution_time = time.time() - start_time
    print(f'Query executed in {execution_time} seconds')

    return raw_data
