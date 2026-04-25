
import time

start_time = time.time()
raw_data = db.executesql(query, as_dict=True)
duration = time.time() - start_time
print(f"Query executed in: {duration} seconds")
