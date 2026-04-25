
from gluon import cache

def cached_get_raw_data():
    key = 'raw_data_query'
    raw_data = cache.ram(key, lambda: dbs.executesql(query, as_dict=True), time_expire=60)
    return raw_data
