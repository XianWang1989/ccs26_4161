
import time

def execute_query(query):
    start_time = time.time()
    result = db.executesql(query, as_dict=True)
    end_time = time.time()
    print(f"Query executed in {end_time - start_time:.2f} seconds")
    return result

# Example usage
query = "SELECT * FROM your_table WHERE conditions..."
data = execute_query(query)
