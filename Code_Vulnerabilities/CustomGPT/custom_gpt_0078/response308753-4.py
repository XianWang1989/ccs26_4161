
from gluon import current
import time

# Assume db is already initialized with connection pooling
def fetch_data(query):
    start_time = time.time()
    raw_data = current.db.executesql(query, as_dict=True)
    end_time = time.time()
    print(f"Query executed in {end_time - start_time:.4f} seconds")
    return raw_data

# Example query
query = "SELECT * FROM your_table WHERE condition = 'value';"
data = fetch_data(query)
