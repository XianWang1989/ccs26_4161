
from gluon import DAL
import time

# Use connection pooling
db = DAL('mysql://user:password@localhost/dbname?pool_size=10')

def execute_query(query):
    start_time = time.time()
    raw_data = db.executesql(query, as_dict=True)
    print(f"Query executed in {time.time() - start_time:.4f} seconds")
    return raw_data

# Example SQL query
query = """
SELECT TIMESTAMPDIFF(...) AS duration,
       TIMESTAMPDIFF(...) - INTERVAL 1 HOUR, TIMESTAMP(...) + INTERVAL CAST(...) AS 'timediff',
       ris.ODATE as 'date',
       CONCAT(...) as 'service'
FROM ... AS ris
JOIN ... as sd on ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
  AND ris.... != '0000-00-00 00:00:00'
  AND ris.... >= '2010-8-15'
  AND ris.... <= '2014-8-22'
"""

# Execute and time the query
execute_query(query)
