
import time
from gluon import DAL

db = DAL('mysql://user:password@host/dbname', pool_size=5)

def execute_query(query):
    start_time = time.time()
    raw_data = db.executesql(query, as_dict=True)
    execution_time = time.time() - start_time
    print(f"Execution time: {execution_time:.4f} seconds")
    return raw_data

query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       ris.ODATE as 'date',
       CONCAT(...) as 'service'
FROM ... AS ris
JOIN ... as sd on ris.... = sd....
WHERE ...
"""
# Execute the query multiple times
for i in range(3):
    execute_query(query)
