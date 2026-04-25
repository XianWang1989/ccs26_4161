
import time
from gluon.debug import dbg

# Define your SQL query
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       TIMESTAMPDIFF(...) - INTERVAL 1 HOUR, 
       TIMESTAMP(...) + INTERVAL CAST(...) AS 'timediff',
       ris.ODATE AS 'date',
       CONCAT(...) AS 'service'
FROM ... AS ris
JOIN ... AS sd ON ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
AND ris.... >= '2010-08-15'
AND ris.... <= '2014-08-22'
"""

# Measure the performance using debug
start_time = time.time()
raw_data = dbs.executesql(query, as_dict=True)  # Initial execution
end_time = time.time()
print(f"Initial execution time: {end_time - start_time:.2f} seconds")

# Set debug to see if performance changes
dbg.set_trace()  # Switch to debug console

# Execute again to compare
start_time = time.time()
raw_data = dbs.executesql(query, as_dict=True)  # Execution in debug mode
end_time = time.time()
print(f"Execution time in debug: {end_time - start_time:.2f} seconds")

# Optionally, execute multiple times to assess any caching effects
for _ in range(3):
    start_time = time.time()
    raw_data = dbs.executesql(query, as_dict=True)  # Multiple executions
    end_time = time.time()
    print(f"Repeated execution time: {end_time - start_time:.2f} seconds")
