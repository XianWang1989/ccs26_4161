
from gluon import current

def get_raw_data(query):
    db = current.db
    # Example: Ensuring the same query is executed with a prepared statement
    raw_data = db.executesql(query, as_dict=True)
    return raw_data

# Example usage
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration', 
           TIMESTAMPDIFF(...) - INTERVAL 1 HOUR, 
           ris.ODATE as 'date',
           CONCAT(...) as 'service'
    FROM ... AS ris
    JOIN ... as sd ON ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
      AND ris.... != '0000-00-00 00:00:00'
      AND ris.... >= '2010-08-15'
      AND ris.... <= '2014-08-22'
"""
data = get_raw_data(query)
