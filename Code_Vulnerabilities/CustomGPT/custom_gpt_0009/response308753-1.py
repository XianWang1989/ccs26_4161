
from gluon import current

# Ensure to set up configuration here
current.db = current.Database('mysql://user:password@host:port/db_name')
current.db._db = current.db.connection
