
from gluon import *
from gluon.dal import DAL

# Set up your database connection with pooling
db = DAL('mysql://username:password@localhost/dbname', pool_size=10)

def execute_query(query):
    try:
        # Measure execution time
        import time
        start_time = time.time()

        # Execute the query
        raw_data = db.executesql(query, as_dict=True)

        elapsed_time = time.time() - start_time
        print(f"Query executed in: {elapsed_time:.2f} seconds")
        return raw_data
    except Exception as e:
        print("An error occurred:", e)
        return None

# Example usage
query = "SELECT * FROM your_table WHERE condition"
data = execute_query(query)

# Handle the data as needed
