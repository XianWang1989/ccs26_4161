
import time
from gluon import current

def run_sql_query(query):
    db = current.db
    start_time = time.time()

    raw_data = db.executesql(query, as_dict=True)

    duration = time.time() - start_time
    current.log("Query executed in: {:.2f} seconds".format(duration))

    return raw_data

query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       ...
FROM ... AS ris
JOIN ... as sd ON ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
AND ris.... >= '2010-8-15'
AND ris.... <= '2014-8-22'
"""

data = run_sql_query(query)
