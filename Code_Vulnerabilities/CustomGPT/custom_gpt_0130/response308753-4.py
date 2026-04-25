
def fetch_data():
    db = DAL('mysql://user:password@localhost/dbname', pool_size=10, migrate=True)

    query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration', ...
    FROM ... AS ris
    JOIN ... as sd on ris.... = sd....
    WHERE ...
    """

    # Use caching to improve performance
    raw_data = cache.ram('my_query_cache_key', 
                         lambda: db.executesql(query, as_dict=True), 
                         time_expire=60)

    return raw_data
