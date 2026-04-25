
from gluon.debug import dbg
import time

start_time = time.time()
raw_data = db.executesql(query, as_dict=True)
elapsed_time = time.time() - start_time
print(f"Elapsed time: {elapsed_time} seconds")
