
from gluon.cache import cache
raw_data = cache.ram('query_key', lambda: dbs.executesql(query, as_dict=True), time_expire=300)
