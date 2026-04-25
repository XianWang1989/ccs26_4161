
import time
from gluon import current

def run_query(query):
    db = current.db
    db.connect()  # Ensure connection

    start_time = time.time()
    try:
        # Execute your raw SQL query
        raw_data = db.executesql(query, as_dict=True)
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        execution_time = time.time() - start_time
        print(f"Execution Time: {execution_time} seconds")

    return raw_data

# Example usage
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       ris.ODATE AS 'date',
       CONCAT(...) AS 'service'
FROM ... AS ris
JOIN ... AS sd ON ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
AND ris.... >= '2010-08-15'
AND ris.... <= '2014-08-22'
"""

result = run_query(query)
