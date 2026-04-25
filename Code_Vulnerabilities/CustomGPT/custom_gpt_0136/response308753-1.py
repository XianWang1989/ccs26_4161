
from gluon import current

db = current.db
db.close()  # Close the connection if open
db.connect()  # Re-establish connection
