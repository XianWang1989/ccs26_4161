
# In your web2py model
db = DAL('mysql://user:password@localhost/db_name', pool_size=10, migrate=True)
