
from gluon import DAL

db = DAL('mysql://user:password@host/dbname', pool_size=10)
