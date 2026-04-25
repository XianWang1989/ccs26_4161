
from gluon import DAL

db = DAL('mysql://user:password@host/database', pool_size=10)
