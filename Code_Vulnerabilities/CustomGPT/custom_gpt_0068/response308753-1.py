
from gluon import current

# Using the current database connection
db = current.db

# Measure execution time of a query in the web context
import time

# Function to execute a raw SQL query and measure execution time
def execute_query(query):
    start_time = time.time()
    result = db.executesql(query, as_dict=True)
    execution_time = time.time() - start_time
    print(f'Execution time: {execution_time} seconds')
    return result

# Example query (replace with your query)
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           TIMESTAMPDIFF(...) AS 'timediff'
    FROM your_table
    WHERE your_conditions
"""

# Execute query in web context
raw_data = execute_query(query)

# Optionally set a breakpoint to debug further
from gluon.debug import dbg
dbg.set_trace()

# Execute query again in debug context
raw_data_debug = execute_query(query)
