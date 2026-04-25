
from gluon import DAL

# Initialize database connection with a connection pool
db = DAL('mysql://user:password@host/dbname', pool_size=10)

def execute_query(some_id):
    # Use a prepared statement to execute the query
    query = "SELECT * FROM my_table WHERE id = %s"
    raw_data = db.executesql(query, (some_id,), as_dict=True)  # Pass parameters as a tuple
    return raw_data

# Example usage
data = execute_query(1)
