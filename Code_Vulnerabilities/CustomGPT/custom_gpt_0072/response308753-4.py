
import time

start_time = time.time()
raw_data = db.executesql(query, as_dict=True)
print("Execution Time: ", time.time() - start_time)
