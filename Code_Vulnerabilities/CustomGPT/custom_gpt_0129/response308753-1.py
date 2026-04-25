
# Assuming 'db' is your database connection in web2py

# Wrap the execution in a context manager to properly handle connections
from gluon import current

def execute_query(query, as_dict=True):
    db = current.db
    # Start a connection
    with db.connection:
        # Execute the SQL command
        result = db.executesql(query, as_dict=as_dict)
    return result

# Usage example:
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       TIMESTAMPDIFF(...) - INTERVAL 1 HOUR, TIMESTAMP(...) + INTERVAL CAST(...) AS 'timediff',
       ris.ODATE as 'date', 
       CONCAT(...) as 'service'
FROM ... AS ris
JOIN ... as sd on ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
AND ris.... != '0000-00-00 00:00:00'
AND ris.... >= '2010-8-15'
AND ris.... <= '2014-8-22'
"""

# Call the function
raw_data = execute_query(query)
