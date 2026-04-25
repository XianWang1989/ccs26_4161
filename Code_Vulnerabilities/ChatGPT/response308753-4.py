
from gluon import current, DAL

# Configure a connection with connection pooling
db = DAL('mysql://user:password@host/dbname', pool_size=10)

def execute_query(query):
    # Using prepared statements
    return db.executesql(query, as_dict=True)

# Sample query
query = """SELECT * FROM your_table WHERE your_condition;"""

# Initial execution
raw_data = execute_query(query)
print(raw_data)

# Using transactions for multiple query executions
with db.transaction():
    raw_data1 = execute_query(query)
    raw_data2 = execute_query(query)  # Use it multiple times as needed

# Debugging through the console
from gluon.debug import dbg
dbg.set_trace()
