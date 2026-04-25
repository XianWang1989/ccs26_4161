
import time
from gluon import current

# Simulate the database execution function for clarity
def execute_query_and_time(query):
    db = current.db
    start_time = time.time()  # Start timing

    # Execute the raw SQL query
    results = db.executesql(query)

    end_time = time.time()  # End timing
    execution_time = end_time - start_time  # Calculate execution duration

    print(f"Query executed in: {execution_time:.4f} seconds")
    return results

query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
    TIMESTAMPDIFF(...) - INTERVAL 1 HOUR, TIMESTAMP(...) + INTERVAL CAST(...) AS 'timediff',
    ris.ODATE as 'date',
    CONCAT(...) as 'service'
FROM ... AS ris
JOIN ... as sd on ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
    AND ris.... != '0000-00-00 00:00:00'
    AND ris.... >= '2010-8-15'
    AND ris.... <= '2014-8-22'
"""

# Execute the query with timing
raw_data = execute_query_and_time(query)

# For further comparisons or testing
raw_data_again = execute_query_and_time(query)
