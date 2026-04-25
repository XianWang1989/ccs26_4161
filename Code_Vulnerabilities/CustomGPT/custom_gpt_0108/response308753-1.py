
from gluon import current
import time

def execute_query(query):
    db = current.db
    start_time = time.time()

    # Execute the SQL query
    result = db.executesql(query, as_dict=True)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Query executed in: {execution_time:.4f} seconds")

    return result

# Example usage
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       ris.ODATE as 'date',
       CONCAT(...) as 'service'
FROM ... AS ris
JOIN ... as sd on ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
      AND ris.... &gt;= '2010-8-15'
      AND ris.... &lt;= '2014-8-22'
"""

# Call the function to execute and measure the query
raw_data = execute_query(query)
