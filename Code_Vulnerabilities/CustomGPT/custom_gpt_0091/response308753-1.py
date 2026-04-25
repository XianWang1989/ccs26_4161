
import time

start_time = time.time()
raw_data = dbs.executesql(query, as_dict=True)
end_time = time.time()
print(f"Query execution time: {end_time - start_time} seconds")
