
from gluon import current

# Before running your query, check if a connection is established
db = current.db

# Ensure connection is set (optional, depending on your configuration)
if not db._uri:
    db.connect()

# Now run your query
query = "SELECT ... FROM ..."
raw_data = db.executesql(query, as_dict=True)
