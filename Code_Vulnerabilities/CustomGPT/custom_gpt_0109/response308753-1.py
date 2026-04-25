
# Ensure that you are using a persistent connection
db.connect()

# Example query execution with error handling
try:
    # First execution (may be slow)
    raw_data = db.executesql(query, as_dict=True)
    print("First query executed.")

    # Subsequent executions should be faster if caching works
    for i in range(3):
        raw_data = db.executesql(query, as_dict=True)
        print(f"Query {i+1} executed, result count: {len(raw_data)}")

except Exception as e:
    print(f"Database error: {e}")

finally:
    # Optionally close connection if not needed
    db.close()
