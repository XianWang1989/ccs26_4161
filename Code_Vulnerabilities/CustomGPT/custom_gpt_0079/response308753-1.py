
from gluon import current
from gluon.debug import dbg

# Function to execute a query with timing
def execute_query(query):
    start_time = current.request.now
    result = current.db.executesql(query, as_dict=True)
    elapsed_time = current.request.now - start_time
    print(f"Query executed in {elapsed_time:.2f} seconds")
    return result

# Sample query
query = """
SELECT TIMESTAMPDIFF(...) AS duration,
       ris.ODATE as date,
       CONCAT(...) as service
FROM ... AS ris
JOIN ... as sd ON ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
  AND ris.... >= '2010-8-15'
  AND ris.... <= '2014-8-22'
"""

# Execute query outside debug mode
raw_data = execute_query(query)  # Expected to be slow

# Enable debug to check for performance improvement
dbg.set_trace()
raw_data = execute_query(query)  # Expected to be faster
