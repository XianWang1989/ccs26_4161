
# Check if connection pooling is enabled
from gluon import current

# Ensure to use the same database connection
db = current.db

# Run a raw SQL query
def execute_query(query):
    try:
        # Using executesql() with the connection
        raw_data = db.executesql(query, as_dict=True)
        return raw_data
    except Exception as e:
        # Log any exceptions
        current.log.error(f"Error executing query: {str(e)}")

# Sample SQL query
query = """
SELECT TIMESTAMPDIFF(...), ... 
FROM your_table 
WHERE condition
"""

# First execution
result_1 = execute_query(query)

# Debugging
from gluon.debug import dbg
dbg.set_trace()  # Check performance in debug mode

# Second execution (should be faster)
result_2 = execute_query(query)
