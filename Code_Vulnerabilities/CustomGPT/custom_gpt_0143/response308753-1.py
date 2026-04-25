
# Ensure you import necessary modules
from gluon import SQLDAL
from gluon.globals import current

# Example function to execute SQL query
def execute_query(query):
    db = current.db  # Get the current database instance
    db.connect()  # Explicitly connect if not connected

    # Use a single connection for multiple queries
    try:
        raw_data = db.executesql(query, as_dict=True)
    finally:
        db.close()  # Close the connection after queries are done

    return raw_data

# Example usage
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       ris.ODATE as 'date',
       CONCAT(...) as 'service'
FROM ... AS ris
JOIN ... as sd on ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
AND ris.... >= '2010-8-15'
AND ris.... <= '2014-8-22';
"""

data = execute_query(query)
print(data)
