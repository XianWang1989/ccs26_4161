
# Ensure proper connections
db.connect()

# Clear any cached queries
db._adapter._connection = None  # reset the connection to avoid stale cache

# Run your query
start_time = time.time()
raw_data = db.executesql(your_query, as_dict=True)
duration = time.time() - start_time

# Log duration
print(f"Query executed in: {duration:.2f} seconds")

# If slow, check connection parameters
if duration > 5:
    print("Query took unusually long. Consider checking your database connection settings.")
