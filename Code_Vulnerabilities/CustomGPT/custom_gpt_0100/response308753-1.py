
# Database connection setup with pooling
from gluon import DAL

# Create a database connection
db = DAL('mysql://username:password@localhost/dbname', pool_size=5, migrate_enabled=False)

# Example function to execute query
def execute_query(query):
    # Use a context manager to ensure connection reuse
    with db.connection_for_read() as conn:
        result = conn.executesql(query, as_dict=True)
    return result

# Running your query
query = "SELECT TIMESTAMPDIFF(...) AS 'duration' FROM your_table WHERE ..."
result = execute_query(query)
print(result)
