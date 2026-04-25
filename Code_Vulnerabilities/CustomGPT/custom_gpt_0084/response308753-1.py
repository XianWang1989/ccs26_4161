
def fetch_data():
    query = """
        SELECT TIMESTAMPDIFF(...) AS 'duration',
               TIMESTAMPDIFF(...) - INTERVAL 1 HOUR,
               ris.ODATE as 'date',
               CONCAT(...) as 'service'
        FROM ... AS ris
        JOIN ... as sd ON ris.... = sd....
        WHERE ris.... != '0000-00-00 00:00:00'
          AND ris.... != '0000-00-00 00:00:00'
          AND ris.... >= '2010-8-15'
          AND ris.... <= '2014-8-22'
    """

    import time
    start_time = time.time()

    # Execute SQL query
    raw_data = dbs.executesql(query, as_dict=True)

    elapsed_time = time.time() - start_time
    print(f"Query executed in: {elapsed_time:.2f} seconds")

    # Debugging
    from gluon.debug import dbg
    dbg.set_trace()

    return raw_data
