
from gluon import current
import time

start_time = time.time()
raw_data = db.executesql(query, as_dict=True)
execution_time = time.time() - start_time
print("Execution time:", execution_time)
