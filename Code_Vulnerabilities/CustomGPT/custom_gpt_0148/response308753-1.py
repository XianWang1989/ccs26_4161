
# Configure web2py database connection pooling
db = DAL('mysql://user:password@host/dbname', pool_size=10)

# Example query with prepared statements (for performance)
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           ris.ODATE as 'date',
           CONCAT(...) as 'service'
    FROM ... AS ris
    JOIN ... as sd ON ris.id = sd.id
    WHERE ris.ODATE BETWEEN '2010-08-15' AND '2014-08-22'
      AND ris.ODATE != '0000-00-00 00:00:00'
"""

# Measure performance
import time

start_time = time.time()
raw_data = db.executesql(query, as_dict=True)
execution_time = time.time() - start_time

print(f"Query executed in {execution_time} seconds")

# For debugging
from gluon.debug import dbg
dbg.set_trace()  # Add debug point to analyze further if needed
