
# Import necessary modules
from gluon import current

# Function to execute SQL
def execute_sql(query):
    # Get current database connection
    db = current.db

    # Start timing
    import time
    start_time = time.time()

    # Execute the query
    raw_data = db.executesql(query, as_dict=True)

    # End timing
    execution_time = time.time() - start_time

    # Print execution time for debugging
    print(f"Execution Time: {execution_time:.4f} seconds")

    return raw_data

# Define your query here
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       TIMESTAMPDIFF(...),
       - INTERVAL 1 HOUR, TIMESTAMP(...),
       + INTERVAL CAST(...) AS 'timediff',
       ris.ODATE as 'date',
       CONCAT(...) as 'service'
FROM ... AS ris
JOIN ... as sd on ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
  AND ris.... != '0000-00-00 00:00:00'
  AND ris.... >= '2010-8-15'
  AND ris.... <= '2014-8-22'
"""

# Execute the function and fetch results
results = execute_sql(query)
# Now you can use results variable
