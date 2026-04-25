
# Ensure connection pooling is enabled
db = DAL('mysql://user:password@localhost/dbname', pool_size=10)
