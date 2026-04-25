
import time

start_time = time.time()
raw_data = db.executesql(query, as_dict=True)
print(f"Execution time: {time.time() - start_time} seconds")
