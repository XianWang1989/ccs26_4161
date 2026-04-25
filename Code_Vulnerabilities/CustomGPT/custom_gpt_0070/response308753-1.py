
from gluon import current

db = current.db
db._adapter.enable_connection_pooling()
