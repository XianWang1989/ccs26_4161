
from gluon import DAL
import time

# Set up the database connection
db = DAL('mysql://username:password@localhost/dbname', pool_size=10)

# Define your query
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration'
FROM ...
WHERE ...
"""

# Function to execute the query and measure time
def execute_query(query):
    start_time = time.time()
    raw_data = db.executesql(query, as_dict=True, cacheable=False)
    print("Execution Time: ", time.time() - start_time)
    return raw_data

# Execute the query
results = execute_query(query)
