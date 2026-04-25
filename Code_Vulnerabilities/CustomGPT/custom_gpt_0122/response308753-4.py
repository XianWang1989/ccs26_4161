
import time
from gluon import current

db = current.db
query = "YOUR_SQL_QUERY"

# Measure execution time
start_time = time.time()
try:
    raw_data = db.executesql(query, as_dict=True)
finally:
    elapsed_time = time.time() - start_time
    print(f"Query executed in: {elapsed_time:.2f} seconds")
