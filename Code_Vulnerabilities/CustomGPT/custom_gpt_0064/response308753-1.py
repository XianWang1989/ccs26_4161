
from gluon import current

# Enable connection pooling
db = current.db
db.connect()
