
from gluon import DAL

db = DAL('mysql://user:password@localhost/dbname', pool_size=10, migrate=True)
