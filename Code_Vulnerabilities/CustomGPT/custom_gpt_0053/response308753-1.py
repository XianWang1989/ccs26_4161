
import time

def execute_query(db, query):
    start_time = time.time()
    raw_data = db.executesql(query, as_dict=True)
    elapsed_time = time.time() - start_time
    print(f"Query executed in: {elapsed_time:.2f} seconds")
    return raw_data

# Your SQL query
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       TIMESTAMPDIFF(...)
       - INTERVAL 1 HOUR, TIMESTAMP(...)
       + INTERVAL CAST(...) AS 'timediff',
       ris.ODATE as 'date',
       CONCAT(...) as 'service'
FROM ... AS ris
JOIN ... as sd on ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
AND ris.... != '0000-00-00 00:00:00'
AND ris.... >= '2010-8-15'
AND ris.... <= '2014-8-22'
"""

# Execute your query
result = execute_query(dbs, query)

# For further analysis
print(result)
