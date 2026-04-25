
# Define your database connection with pooling
db = DAL('mysql://username:password@localhost/dbname', pool_size=10, migrate=True)

# Optimize your query if possible
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       TIMESTAMPDIFF(...) - INTERVAL 1 HOUR AS 'timediff',
       ris.ODATE AS 'date',
       CONCAT(...) AS 'service'
FROM ... AS ris
JOIN ... AS sd ON ris.... = sd....
WHERE ris.... IS NOT NULL
AND ris.... BETWEEN '2010-08-15' AND '2014-08-22'
"""

# Execute SQL
import time

start_time = time.time()
raw_data = db.executesql(query, as_dict=True)
execution_time = time.time() - start_time

print(f"Execution time: {execution_time} seconds")
