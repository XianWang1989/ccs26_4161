
from gluon import current

def log_query(query):
    start_time = time.time()
    result = current.db.executesql(query, as_dict=True)
    end_time = time.time()
    print(f"Query: {query} executed in {end_time - start_time:.2f} seconds")
    return result
