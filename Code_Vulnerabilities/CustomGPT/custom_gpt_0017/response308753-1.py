
import time
from gluon import current

db = current.db

# Define your SQL query
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           TIMESTAMPDIFF(...) - INTERVAL 1 HOUR AS 'timestamp_diff',
           ris.ODATE as 'date',
           CONCAT(...) as 'service'
    FROM ... AS ris
    JOIN ... as sd on ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
      AND ris.... &gt;= '2010-8-15'
      AND ris.... &lt;= '2014-8-22'
"""

# Timing the execution
start_time = time.time()
raw_data = db.executesql(query, as_dict=True)
end_time = time.time()

# Log the elapsed time
current.response.write(f"Query executed in {end_time - start_time} seconds")
