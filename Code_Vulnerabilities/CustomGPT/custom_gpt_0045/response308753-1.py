
import time
from gluon import current

# Start a timer
start_time = time.time()

# Begin a transaction
with current.db.transaction():
    # Execute the query
    query = "YOUR SQL QUERY HERE"
    result = current.db.executesql(query, as_dict=True)

# Measure elapsed time
elapsed_time = time.time() - start_time
current.db.commit()  # Ensure that changes are committed

# Output the timing
print(f"Query executed in: {elapsed_time:.2f} seconds")
