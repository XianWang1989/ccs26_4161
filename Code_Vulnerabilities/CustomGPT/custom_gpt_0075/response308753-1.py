
# Example snippet to test the database performance
from gluon import current

# Define your query
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           ris.ODATE as 'date',
           CONCAT(...) as 'service'
    FROM ... AS ris
    JOIN ... as sd ON ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
          AND ris.... >= '2010-8-15'
          AND ris.... <= '2014-8-22'
"""

# Measure execution time
import time

# First execution
start_time = time.time()
raw_data = current.db.executesql(query, as_dict=True)
print("First execution time:", time.time() - start_time)

# Subsequent executions (for testing)
for _ in range(5):
    start_time = time.time()
    raw_data = current.db.executesql(query, as_dict=True)
    print("Subsequent execution time:", time.time() - start_time)
