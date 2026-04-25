
# Ensure your db instance uses connection pooling
from gluon import DAL

# Connect to your database with connection pooling enabled
db = DAL('mysql://user:password@localhost/dbname', pool_size=10)

# Define your query
query = """
    SELECT TIMESTAMPDIFF(...) AS duration,
           TIMESTAMPDIFF(...) - INTERVAL 1 HOUR AS time,
           ris.ODATE AS date,
           CONCAT(...) AS service
    FROM ... AS ris
    JOIN ... AS sd ON ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
      AND ris.... != '0000-00-00 00:00:00'
      AND ris.... >= '2010-08-15'
      AND ris.... <= '2014-08-22'
"""

# Example function to execute the query
def fetch_data(query):
    raw_data = db.executesql(query, as_dict=True)
    return raw_data

# Test the execution time
import time

start_time = time.time()
data = fetch_data(query)
end_time = time.time()

print(f"Query executed in {end_time - start_time:.4f} seconds")
