
from gluon import DAL

db = DAL('mysql://username:password@hostname/database', pool_size=5, migrate=True)
