
from gluon import current

db = current.db
# Initialize connection pooling
db.connect()  # Make sure to connect before executing queries
