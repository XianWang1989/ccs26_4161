
from gluon import DAL

# Create a connection pool. Adjust parameters based on your database configuration.
db = DAL('mysql://username:password@localhost/db_name', pool_size=5, migrate=True)
