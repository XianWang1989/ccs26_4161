
# Configure your database connection with connection pooling
db = DAL('mysql://username:password@host/databasename', pool_size=5)

# Define your query
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       TIMESTAMPDIFF(...) - INTERVAL 1 HOUR,
       TIMESTAMP(...),
       CONCAT(...) AS 'service'
FROM ... AS ris
JOIN ... AS sd ON ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
AND ris.... != '0000-00-00 00:00:00'
AND ris.... >= '2010-8-15'
AND ris.... <= '2014-8-22'
"""

# Example usage of executesql with connection pooling
def run_query():
    raw_data = db.executesql(query, as_dict=True)
    return raw_data

# Test the response time
import time

start_time = time.time()
result = run_query()
print(f"Query executed in: {time.time() - start_time} seconds")

# You can also enable query logging to see how long each query takes
db._adapter.debug = True
