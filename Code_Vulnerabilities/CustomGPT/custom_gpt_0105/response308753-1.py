
import time
from gluon import current

def execute_query_with_timing(query):
    db = current.db
    start_time = time.time()

    # Execute the query
    raw_data = db.executesql(query, as_dict=True)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Query executed in {execution_time:.4f} seconds")

    return raw_data

# Example usage
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

# Execute the query and measure time
data = execute_query_with_timing(query)
