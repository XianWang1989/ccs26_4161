
import time

def log_query_time(query):
    start_time = time.time()
    result = db.executesql(query, as_dict=True)
    duration = time.time() - start_time
    print(f'Query executed in: {duration:.2f} seconds')
    return result

# Use the logging function
data = log_query_time(query)
