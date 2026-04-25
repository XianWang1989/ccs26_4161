
import time

# Define your query
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       TIMESTAMPDIFF(...) - INTERVAL 1 HOUR,
       ris.ODATE AS 'date',
       CONCAT(...) AS 'service'
FROM ... AS ris
JOIN ... AS sd ON ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
AND ris.... >= '2010-8-15'
AND ris.... <= '2014-8-22'
"""

# Measure execution time in main application context
start_time = time.time()
raw_data = dbs.executesql(query, as_dict=True)
print(f"Main execution time: {time.time() - start_time:.2f} seconds")

# Using debug console
from gluon.debug import dbg
dbg.set_trace()  # Enter debug mode
raw_data = dbs.executesql(query, as_dict=True)
print(f"Debug execution time: {time.time() - start_time:.2f} seconds")
