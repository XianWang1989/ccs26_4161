
# Assuming 'dbs' is your database object
from gluon.debug import dbg

# Initial query execution
query = "SELECT YOUR_FIELDS_HERE FROM YOUR_TABLE WHERE YOUR_CONDITIONS"
raw_data = dbs.executesql(query, as_dict=True)  # Slow execution

# Profiling execution time
import time

start_time = time.time()
raw_data = dbs.executesql(query, as_dict=True)
elapsed_time = time.time() - start_time
print(f"First execution time: {elapsed_time:.2f} seconds")

# Debugging console to check performance
dbg.set_trace()

# Subsequent execution after going to debug console
start_time = time.time()
raw_data = dbs.executesql(query, as_dict=True)  # Fast execution
elapsed_time = time.time() - start_time
print(f"Execution time in debug console: {elapsed_time:.2f} seconds")

# Check timings
print(dbs._timings)
