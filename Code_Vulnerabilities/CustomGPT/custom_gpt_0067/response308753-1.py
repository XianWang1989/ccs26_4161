
# Ensure pooling is enabled in your web2py model file (models/db.py)
from gluon import DAL

# Example of setting up a connection with connection pooling
dbs = DAL('mysql://username:password@localhost/dbname', pool_size=10)

# Sample function to execute a query with timing
import time

def execute_query(query):
    start_time = time.time()
    result = dbs.executesql(query, as_dict=True)
    elapsed_time = time.time() - start_time
    print(f"Query executed in {elapsed_time:.4f} seconds")
    return result

# Sample query
query = """
SELECT TIMESTAMPDIFF(...) AS duration
FROM ... AS ris
JOIN ... AS sd ON ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
AND ris.... >= '2010-08-15'
AND ris.... <= '2014-08-22'
"""

# Execute the query
raw_data = execute_query(query)
