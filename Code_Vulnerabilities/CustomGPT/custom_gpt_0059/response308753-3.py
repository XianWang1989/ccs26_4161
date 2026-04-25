
from gluon import current
import time

def execute_query(query):
    db = current.db
    timing_data = {}

    start_time = time.time()
    raw_data = db.executesql(query, as_dict=True)
    timing_data['raw_execution_time'] = time.time() - start_time

    return raw_data, timing_data

query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration', ris.ODATE as 'date'
    FROM ... AS ris
    WHERE ris.... != '0000-00-00 00:00:00'
      AND ris.... >= '2010-08-15'
      AND ris.... <= '2014-08-22'
"""
data, timings = execute_query(query)
print("Query Timings:", timings)
