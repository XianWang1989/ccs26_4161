
from gluon import cache

query = "SELECT ... FROM ..."
cached_data = cache.ram('my_query_cache', lambda: db.executesql(query, as_dict=True), time_expire=300)
