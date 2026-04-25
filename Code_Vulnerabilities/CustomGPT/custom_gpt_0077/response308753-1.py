
from gluon import current

def execute_query(query):
    db = current.db
    from datetime import datetime

    start_time = datetime.now()
    raw_data = db.executesql(query, as_dict=True)
    end_time = datetime.now()

    execution_time = (end_time - start_time).total_seconds()
    print(f"Query executed in {execution_time} seconds")

    return raw_data

# Example usage
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       ...
FROM ... AS ris
JOIN ... as sd ON ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
  AND ris.... &gt;= '2010-8-15'
  AND ris.... &lt;= '2014-8-22'
"""
raw_data = execute_query(query)
