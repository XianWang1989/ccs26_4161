
from gluon import current
db = current.db
db._uri = 'mysql://user:pass@host/dbname'
db._pool = db._get_pool(5)  # Adjust pool size as needed
