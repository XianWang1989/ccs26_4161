
# Optimize the connection settings
db = DAL('mysql://username:password@localhost/database_name', pool_size=10)

# Use a context manager for raw SQL execution
def execute_query(query):
    with db.connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

# Execute the query
query = "YOUR SQL QUERY HERE"  # Replace with your actual SQL query
raw_data = execute_query(query)
