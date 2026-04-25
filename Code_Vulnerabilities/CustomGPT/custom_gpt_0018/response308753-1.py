
import time

# Function to execute and time the SQL query
def execute_and_time_query(query):
    start_time = time.time()  # Start time
    raw_data = db.executesql(query, as_dict=True)  # Execute the query
    execution_time = time.time() - start_time  # Calculate execution time

    print(f"Query executed in: {execution_time:.4f} seconds")
    return raw_data

# Example SQL query
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           TIMESTAMPDIFF(...) - INTERVAL 1 HOUR,
           ris.ODATE as 'date',
           CONCAT(...) as 'service'
    FROM ... AS ris
    JOIN ... as sd on ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
      AND ris.... >= '2010-8-15'
      AND ris.... <= '2014-8-22'
"""

# Call the function to execute and time the query
raw_data = execute_and_time_query(query)
