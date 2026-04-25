
from gluon import cache

# Cache the result for 10 minutes
cached_query = cache.ram('unique_key_for_query', lambda: dbs.executesql(query, as_dict=True), timeexp=600)
