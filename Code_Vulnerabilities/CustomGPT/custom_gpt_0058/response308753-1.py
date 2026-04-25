
# In models/db.py, ensure your database is set up for pooling
from gluon import DAL

# Connection pooling
db = DAL('mysql://username:password@localhost/databasename', auto_import=True)

# Example usage with a cached query
def fetch_data():
    cached_data = cache.ram('fetch_data_key', 
        lambda: db.executesql("SELECT * FROM your_table"), 
        time_expire=300) # Cache for 5 minutes
    return cached_data
