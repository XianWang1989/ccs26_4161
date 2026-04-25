
from gluon import *

# Initialize database with connection pooling
db = DAL('mysql://username:password@localhost/dbname', pool_size=10)

# Your query
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       TIMESTAMPDIFF(...) - INTERVAL 1 HOUR,
       ris.ODATE as 'date',
       CONCAT(...) as 'service'
FROM ... AS ris
JOIN ... as sd on ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
AND ris.... >= '2010-08-15'
AND ris.... <= '2014-08-22'
"""

# Execute with timing
import time

start_time = time.time()
raw_data = db.executesql(query, as_dict=True)
print(f"Query executed in {time.time() - start_time} seconds")
