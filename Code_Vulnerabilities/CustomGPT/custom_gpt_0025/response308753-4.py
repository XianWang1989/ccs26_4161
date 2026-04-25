
import time
from gluon import current

def execute_query(query):
    start_time = time.time()
    result = current.db.executesql(query, as_dict=True)
    duration = time.time() - start_time
    current.logger.info(f"Executed query in {duration:.2f} seconds: {query}")
    return result

# Usage
query = "SELECT * FROM your_table WHERE conditions..."
data = execute_query(query)
