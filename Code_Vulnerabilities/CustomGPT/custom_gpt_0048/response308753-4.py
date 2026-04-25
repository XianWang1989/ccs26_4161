
from gluon.debug import dbg

# Function to run the query and debug timing
def debug_timed_query(dbs, query):
    import time
    start_time = time.time()
    raw_data = dbs.executesql(query, as_dict=True)
    duration = time.time() - start_time
    print(f"Query duration: {duration} seconds")
    return raw_data

dbg.set_trace()  # Set this at the beginning of your process
data = debug_timed_query(dbs, your_query_here)
