
from gluon import current

# Check if using the same connection
db = current.db

# Use db.connect() to force a connection (if needed)
if not db.connection:
    db.connect()

raw_data = db.executesql(query, as_dict=True) 
