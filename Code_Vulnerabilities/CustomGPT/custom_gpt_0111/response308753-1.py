
from gluon import current

# Assuming 'db' is your database connection
db = current.db

# Example query
query = """
    SELECT TIMESTAMPDIFF(MINUTE, ris.ODATE, NOW()) AS duration,
           ris.ODATE as date,
           CONCAT(ris.service_id, ' - ', ris.service_name) as service
    FROM your_table AS ris
    WHERE ris.ODATE IS NOT NULL
    AND ris.ODATE >= '2010-08-15' 
    AND ris.ODATE <= '2014-08-22'
"""

# Setting options for connection pooling if not already set
if not db._pool:
    db._pool = True  # Enable connection pooling

# Execute query
try:
    raw_data = db.executesql(query, as_dict=True)
    print(raw_data)
except Exception as e:
    print("Error executing query:", e)
