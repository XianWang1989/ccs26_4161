
import time

start_time = time.time()
raw_data = db.executesql(query, as_dict=True)  # This takes long
elapsed_time = time.time() - start_time
print(f"Elapsed time for first query: {elapsed_time} seconds")

# Followed by more queries in the same block or context
start_time = time.time()
raw_data = db.executesql(query, as_dict=True)  # Subsequent queries
elapsed_time = time.time() - start_time
print(f"Elapsed time for second query: {elapsed_time} seconds")
