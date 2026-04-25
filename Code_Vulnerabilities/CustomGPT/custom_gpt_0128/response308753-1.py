
import time
from gluon import current

def execute_query_and_time(query):
    start_time = time.time()
    raw_data = current.db.executesql(query, as_dict=True)
    elapsed_time = time.time() - start_time
    print(f"Query executed in: {elapsed_time:.2f} seconds")
    return raw_data

def check_connection_status():
    # Check the current connection
    print(f"Connection info: {current.db._uri}")

# Example usage
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           ris.ODATE as 'date',
           CONCAT(...) as 'service'
    FROM ... AS ris
    JOIN ... as sd on ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
          and ris.... >= '2010-8-15'
          and ris.... <= '2014-8-22'
"""

check_connection_status()
execute_query_and_time(query)
