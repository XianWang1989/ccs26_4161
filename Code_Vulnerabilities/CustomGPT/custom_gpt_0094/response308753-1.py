
def optimized_query():
    # Define your query
    query = """
        SELECT TIMESTAMPDIFF(...) AS 'duration', ris.ODATE as 'date', CONCAT(...) as 'service'
        FROM ... AS ris
        JOIN ... as sd on ris.... = sd....
        WHERE ris.... != '0000-00-00 00:00:00'
        AND ris.... >= '2010-8-15' AND ris.... <= '2014-8-22'
    """

    # Cache the result for 60 seconds
    cached_data = cache.ram('optimized_query_cache', lambda: db.executesql(query, as_dict=True), time_expire=60)

    return cached_data
