
import time

def timed_execute_query(query):
    start_time = time.time()
    result = db.executesql(query, as_dict=True)
    execution_time = time.time() - start_time
    print(f"Query executed in {execution_time:.2f} seconds")
    return result
