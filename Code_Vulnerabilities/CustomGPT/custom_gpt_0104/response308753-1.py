
from gluon import current
from time import time

def execute_query(query):
    db = current.db

    # Time the query execution
    start_time = time()
    raw_data = db.executesql(query, as_dict=True)
    end_time = time()

    # Log the execution time
    execution_time = end_time - start_time
    print(f"Query executed in {execution_time:.2f} seconds")
    return raw_data

# Your query
my_query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       TIMESTAMPDIFF(...) - INTERVAL 1 HOUR, TIMESTAMP(...)
FROM ... AS ris
JOIN ... as sd on ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
  AND ris.... != '0000-00-00 00:00:00'
  AND ris.... >= '2010-8-15'
  AND ris.... <= '2014-8-22'
"""

# Call the function
execute_query(my_query)
