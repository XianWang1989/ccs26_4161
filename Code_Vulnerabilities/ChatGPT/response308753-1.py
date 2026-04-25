
from gluon import current

# Configure your database connection with connection pooling
current.db = DAL('mysql://user:password@host/dbname', pool_size=10)
