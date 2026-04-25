
from gluon import current

# Fetch the database object
db = current.db

# Function to execute SQL with proper context management
def execute_query(query, params=None):
    # Explicitly use a connection
    with db.connection:
        db.executesql("SET SESSION wait_timeout = 600")  # Adjust session settings if needed
        results = db.executesql(query, as_dict=True, *params if params else [])
    return results

# Example usage
query = """
SELECT TIMESTAMPDIFF(DAY, ris.ODATE, NOW()) AS 'duration',
       ris.ODATE AS 'date',
       CONCAT(sd.service, ' - ', ris.ODATE) AS 'service'
FROM ... AS ris
JOIN ... AS sd ON ris.id = sd.id
WHERE ris.ODATE IS NOT NULL
AND ris.ODATE >= '2010-08-15'
AND ris.ODATE <= '2014-08-22'
"""

# Execute the query
try:
    raw_data = execute_query(query)
    print(raw_data)
except Exception as e:
    print("Error executing query:", e)
