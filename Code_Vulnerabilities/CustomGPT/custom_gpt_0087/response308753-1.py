
# Import necessary components from web2py
from gluon import current
from time import time

# Function to execute a raw SQL query
def execute_query(query):
    db = current.db  # Use the globally available database object

    start_time = time()
    raw_data = db.executesql(query, as_dict=True)
    duration = time() - start_time

    print(f"Query executed in {duration:.3f} seconds")
    return raw_data

# Example usage
query = """SELECT TIMESTAMPDIFF(SECOND, start_time, end_time) AS 'duration'
           FROM your_table
           WHERE some_conditions"""

# First execution
results1 = execute_query(query)

# Potentially run the same query again to check performance
results2 = execute_query(query)

# Debugging with the interactive console
if current.request.controller == 'your_controller_name':
    from gluon.debug import dbg
    dbg.set_trace()  # Triggers debug mode for faster execution
