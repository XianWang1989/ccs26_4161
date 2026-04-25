
from gluon import DAL
from gluon.debug import dbg

# Set up the database connection with pooling
db = DAL('mysql://user:password@localhost/dbname', pool_size=10, migrate=True)

def execute_query(query):
    raw_data = None
    # Use a transaction for multiple queries
    with db.transaction():
        raw_data = db.executesql(query, as_dict=True)
    return raw_data

# Sample usage
dbg.set_trace()  # Start debugging
query = "SELECT ... FROM ... WHERE ...;"
result = execute_query(query)  # Should be faster in this setup
