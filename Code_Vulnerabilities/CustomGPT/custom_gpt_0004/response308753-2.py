
import time

start_time = time.time()
raw_data = db.executesql(query, as_dict=True)
end_time = time.time()
print(f"Query executed in {end_time - start_time} seconds")
