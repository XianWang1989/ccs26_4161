
from gluon import current

# Use a context manager to ensure proper connection handling
def execute_query(query):
    db = current.db
    with db.connection as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results

# Your specific query
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           TIMESTAMPDIFF(...) - INTERVAL 1 HOUR, TIMESTAMP(...),
           ris.ODATE as 'date',
           CONCAT(...) as 'service'
    FROM ... AS ris
    JOIN ... AS sd ON ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
      AND ris.... >= '2010-8-15'
      AND ris.... <= '2014-8-22';
"""

# Call the function to execute the query
raw_data = execute_query(query)
