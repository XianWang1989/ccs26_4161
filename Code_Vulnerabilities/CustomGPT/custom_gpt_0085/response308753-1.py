
# models/db.py
import pymysql
from gluon import DAL

# Database settings with connection pooling
db = DAL('mysql://username:password@localhost/dbname', pool_size=10)

def execute_optimized_query(query):
    """
    Execute the SQL query and log timing for performance analysis.
    """
    import time
    start_time = time.time()

    results = db.executesql(query, as_dict=True)

    end_time = time.time()
    print(f"Query executed in {end_time - start_time:.3f} seconds.")

    return results

# Example usage in your controller
def my_controller_function():
    query = "SELECT ... FROM ... WHERE conditions..."
    raw_data = execute_optimized_query(query)
    return dict(data=raw_data)
