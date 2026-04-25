
import time
from gluon import current

def execute_query(query):
    db = current.db
    start_time = time.time()

    # Execute the query
    raw_data = db.executesql(query, as_dict=True)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Query executed in {elapsed_time:.2f} seconds")
    return raw_data

# Example Usage
query = """
SELECT TIMESTAMPDIFF(...), ris.ODATE as 'date', CONCAT(...) as 'service'
FROM ... AS ris
JOIN ... as sd ON ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00' AND ris.... >= '2010-8-15' AND ris.... <= '2014-8-22'
"""
result = execute_query(query)
