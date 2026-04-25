
def get_data():
    query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration', ...
    FROM ... AS ris
    JOIN ... as sd ON ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
      AND ris.... >= '2010-8-15'
      AND ris.... <= '2014-8-22';
    """
    # Use caching to improve performance
    cache_time = 60  # cache for 1 minute
    raw_data = cache.ram('query_data', lambda: db.executesql(query, as_dict=True), cache_time)

    return raw_data

# Example usage
data = get_data()
