
from gluon import DAL, Field
from datetime import datetime

# Initialize database connection
db = DAL('mysql://username:password@host:port/database')

# Query for testing
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           TIMESTAMPDIFF(...) - INTERVAL 1 HOUR, TIMESTAMP(...) + INTERVAL CAST(...) AS 'timediff',
           ris.ODATE AS 'date',
           CONCAT(...) AS 'service'
    FROM ... AS ris
    JOIN ... AS sd ON ris.... = sd....
    WHERE ris.... NOT IN ('0000-00-00 00:00:00')
      AND ris.... >= '2010-08-15'
      AND ris.... <= '2014-08-22'
"""

# Execute query and measure performance
import time

start_time = time.time()
raw_data = db.executesql(query, as_dict=True)
print("Execution time:", time.time() - start_time)

# Run the query multiple times and log execution time
for _ in range(3):
    start_time = time.time()
    raw_data = db.executesql(query, as_dict=True)
    print("Execution time for query:", time.time() - start_time)

# Optional: Add connection closing if necessary
db.close()
