
from gluon import current
db = current.db

# Use the same connection throughout the request cycle
with db.connection:
    raw_data = db.executesql(query, as_dict=True)
