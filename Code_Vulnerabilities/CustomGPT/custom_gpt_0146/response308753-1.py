
# Assuming 'dbs' is your database connection
from gluon import current, cache

def get_data(query):
    # Here we use cache. The 'tariff' parameter determines the cache key
    cache_key = "data_query_" + str(hash(query))
    cached_result = cache.ram(cache_key, lambda: dbs.executesql(query, as_dict=True), time_expire=300)

    return cached_result

def your_controller_function():
    query = """
        SELECT TIMESTAMPDIFF(...) AS 'duration',
               ris.ODATE as 'date',
               CONCAT(...) as 'service'
        FROM ... AS ris
        JOIN ... as sd ON ris.... = sd....
        WHERE ris.... != '0000-00-00 00:00:00'
          AND ris.... >= '2010-8-15'
          AND ris.... <= '2014-8-22'
    """

    # Retrieving data using the caching function
    raw_data = get_data(query)

    # Process raw_data as needed
    return dict(data=raw_data)
