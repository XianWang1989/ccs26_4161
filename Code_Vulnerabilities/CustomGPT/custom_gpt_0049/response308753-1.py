
# Example of testing query performance with connection pooling

# Start by setting up the necessary imports
from gluon import current
from gluon.debug import dbg
import time

# Your SQL query
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           TIMESTAMPDIFF(...) - INTERVAL 1 HOUR,
           ... 
    FROM ... AS ris
    JOIN ... as sd on ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
          AND ris.... &gt;= '2010-8-15'
          AND ris.... &lt;= '2014-8-22'
"""

# Using dbs and db.executesql() to track timings
start_time = time.time()
raw_data = dbs.executesql(query, as_dict=True)  # Regular execution
print(f"Execution time: {time.time() - start_time} seconds")

# Debugging with the web2py debug console
dbg.set_trace()  # Set a breakpoint here

# Re-execute query to see if there's a difference in performance
start_time = time.time()
raw_data_debug = dbs.executesql(query, as_dict=True)  # Execution post debug breakpoint
print(f"Execution time after debug: {time.time() - start_time} seconds")
