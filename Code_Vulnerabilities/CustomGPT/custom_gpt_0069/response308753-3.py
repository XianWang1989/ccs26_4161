
from gluon import cache

def fetch_data():
    query = """
    SELECT TIMESTAMPDIFF(...) AS duration,
           TIMESTAMPDIFF(...) - INTERVAL 1 HOUR, 
           ris.ODATE as date,
           CONCAT(...) as service
    FROM ... AS ris
    JOIN ... AS sd ON ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
      AND ris.... >= '2010-08-15'
      AND ris.... <= '2014-08-22'
    """

    # Using caching
    cached_data = cache.ram('my_query_cache', 
                             lambda: db.executesql(query, as_dict=True), 
                             time_expire=300)
    return cached_data

data = fetch_data()
