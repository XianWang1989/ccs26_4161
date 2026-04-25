
import time

# Sample query (adapt to your actual query)
query = """
SELECT TIMESTAMPDIFF(...), ris.ODATE as 'date'
FROM ... AS ris
JOIN ... as sd ON ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
AND ris.... >= '2010-08-15'
AND ris.... <= '2014-08-22'
"""

# Function to measure execution time
def test_query_execution(db, query):
    start_time = time.time()
    result = db.executesql(query, as_dict=True)
    end_time = time.time()
    exec_time = end_time - start_time
    print(f"Query executed in {exec_time:.3f} seconds.")
    return result

# Test execution without debugging
raw_data = test_query_execution(dbs, query)

# Entering debug mode
from gluon.debug import dbg
dbg.set_trace()

# Test execution within debugging
raw_data_debug = test_query_execution(dbs, query)
