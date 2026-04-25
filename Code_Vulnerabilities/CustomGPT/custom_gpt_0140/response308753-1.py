
import time
from gluon import current

def execute_query(query):
    db = current.db
    start_time = time.time()

    # Optionally, ensure that you're using a fresh connection
    # db.connection.close()  # Uncomment if needed
    raw_data = db.executesql(query, as_dict=True)

    duration = time.time() - start_time
    print(f"Query executed in: {duration:.2f} seconds")

    return raw_data

# Example use case
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

# Execute the query
result = execute_query(query)

# Inspect the results
print(result)
