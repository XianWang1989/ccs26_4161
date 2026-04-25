
def optimized_query():
    from gluon import current

    db = current.db
    db._adapter.enable_connection_pooling()

    # Sample query that retrieves data considerably
    query = """
        SELECT TIMESTAMPDIFF(...) AS 'duration',
               ris.ODATE as 'date',
               CONCAT(...) as 'service'
        FROM ... AS ris
        JOIN ... AS sd ON ris.... = sd....
        WHERE ris.... != '0000-00-00 00:00:00'
          AND ris.... >= '2010-08-15'
          AND ris.... <= '2014-08-22'
    """

    try:
        raw_data = db.executesql(query, as_dict=True)
        return raw_data
    except Exception as e:
        # Handle exceptions
        return str(e)
