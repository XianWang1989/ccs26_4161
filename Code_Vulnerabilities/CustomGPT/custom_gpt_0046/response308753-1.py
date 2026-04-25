
# Import necessary libraries
from gluon import current
import time

# Function to execute the query and measure time
def execute_query(query):
    start_time = time.time()
    raw_data = current.db.executesql(query, as_dict=True)
    duration = time.time() - start_time
    print(f"Query executed in {duration} seconds")
    return raw_data

# Example query
query = """
SELECT TIMESTAMPDIFF(...), ris.ODATE as 'date', CONCAT(...) as 'service'
FROM ... AS ris
JOIN ... as sd on ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
AND ris.... >= '2010-8-15'
AND ris.... <= '2014-8-22'
"""

# Execute the query
raw_data = execute_query(query)

# Debugging
from gluon.debug import dbg
dbg.set_trace()  # Check if this changes the execution speed
