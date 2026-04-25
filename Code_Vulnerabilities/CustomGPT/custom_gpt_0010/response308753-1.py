
from gluon import current
from gluon.debug import dbg
import time

# Function to execute a query and time it
def execute_query(query):
    start_time = time.time()
    result = current.db.executesql(query, as_dict=True)
    elapsed_time = time.time() - start_time
    print(f"Query executed in {elapsed_time:.2f} seconds")
    return result

# Example usage
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       TIMESTAMPDIFF(...)
       - INTERVAL 1 HOUR, TIMESTAMP(...)
       + INTERVAL CAST(...) AS 'timediff',
       ris.ODATE as 'date',
       CONCAT(...) as 'service'
FROM ... AS ris
JOIN ... as sd on ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
      AND ris.... != '0000-00-00 00:00:00'
      AND ris.... >= '2010-8-15'
      AND ris.... <= '2014-8-22'
"""

# Execute multiple times to detect performance improvement
for _ in range(3):
    raw_data = execute_query(query)

# Debugging section
dbg.set_trace()  # After this point, check the performance in the debug console
raw_data = execute_query(query)  # Check performance again in the debug console
