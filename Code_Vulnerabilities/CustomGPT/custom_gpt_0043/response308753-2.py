
import time

start_time = time.time()
raw_data = db.executesql(query, as_dict=True)
execution_time = time.time() - start_time
print(f"Query executed in: {execution_time:.2f} seconds")
