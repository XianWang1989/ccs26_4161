
from gluon.debug import dbg
import time

# Before executing a slow query
start_time = time.time()
raw_data = db.executesql(query, as_dict=True)
elapsed_time = time.time() - start_time
print("Elapsed time:", elapsed_time)

dbg.set_trace()  # Check variables and state at this point
