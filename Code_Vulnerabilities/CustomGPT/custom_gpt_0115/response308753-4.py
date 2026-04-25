
from gluon import DAL, Field
from gluon.debug import dbg
import time

# Database connection
db = DAL('mysql://username:password@hostname/database', pool_size=5, migrate=True)

# Example SQL query
query = """
SELECT TIMESTAMPDIFF(...), 
       ris.ODATE, 
       CONCAT(...) AS service
FROM ris
JOIN sd ON ris.id = sd.ris_id
WHERE ris.ODATE IS NOT NULL 
  AND ris.ODATE BETWEEN '2010-08-15' AND '2014-08-22'
"""

# Measure execution time
start_time = time.time()
raw_data = db.executesql(query, as_dict=True)
execution_time = time.time() - start_time
print(f"Query executed in {execution_time:.2f} seconds")

# Debugging interface
dbg.set_trace()
