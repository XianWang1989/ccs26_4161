
import time

def execute_query(db, query):
    start_time = time.time()
    result = db.executesql(query, as_dict=True)
    duration = time.time() - start_time
    print(f"Query executed in {duration:.4f} seconds")
    return result

query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       TIMESTAMPDIFF(...) - INTERVAL 1 HOUR, 
       TIMESTAMP(...) + INTERVAL CAST(...) AS 'timediff',
       ris.ODATE as 'date',
       CONCAT(...) as 'service'
FROM ... AS ris
JOIN ... as sd on ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
AND ris.... &gt;= '2010-8-15'
AND ris.... &lt;= '2014-8-22'
"""

# Usage
raw_data = execute_query(dbs, query)
