
import time
from gluon import current

# Function to execute SQL with timing
def execute_query(query):
    db = current.db  # Get the web2py database instance

    # Timing the query execution
    start_time = time.time()
    raw_data = db.executesql(query, as_dict=True)
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Query executed in: {execution_time:.4f} seconds")
    return raw_data

# Usage of the function
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           ris.ODATE as 'date',
           CONCAT(...) as 'service'
    FROM ... AS ris
    JOIN ... as sd ON ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
          AND ris.... >= '2010-8-15'
          AND ris.... <= '2014-8-22'
"""
result = execute_query(query)
