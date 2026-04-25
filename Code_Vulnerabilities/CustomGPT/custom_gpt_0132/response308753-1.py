
# Ensure that you are using persistent connections
from gluon import DAL, Field

# Connect to the database using a persistent connection
db = DAL('mysql://username:password@localhost/dbname', pool_size=10)

# Example query
query = """
SELECT TIMESTAMPDIFF(...), ris.ODATE, CONCAT(...)
FROM ... AS ris
JOIN ... AS sd ON ris... = sd...
WHERE ris... != '0000-00-00 00:00:00'
  AND ris... >= '2010-08-15'
  AND ris... <= '2014-08-22'
"""

# Time the execution of the query
import time

start_time = time.time()
raw_data = db.executesql(query, as_dict=True)
end_time = time.time()

print(f"Query executed in {end_time - start_time:.4f} seconds")
