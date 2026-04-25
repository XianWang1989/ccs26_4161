
from gluon import current
from gluon.cache import cache

# Setup the database with a pool
db = DAL('mysql://user:password@localhost/dbname', pool_size=10, pool_wait=True)

# Define a query
query = """SELECT ... FROM ... WHERE ..."""

# Use cache to store results for repeat queries
raw_data = cache.ram('my_query_cache', lambda: db.executesql(query, as_dict=True), time_expire=300)

# Debugging to analyze performance
from gluon.debug import dbg
dbg.set_trace()
