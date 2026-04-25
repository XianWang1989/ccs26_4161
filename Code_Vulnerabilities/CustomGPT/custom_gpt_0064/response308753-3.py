
def execute_query():
    query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           TIMESTAMPDIFF(...) - INTERVAL 1 HOUR, TIMESTAMP(...)
    FROM ... AS ris
    JOIN ... as sd ON ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
      AND ris.... >= '2010-8-15'
      AND ris.... <= '2014-8-22'
    """

    # Enable connection pooling
    db = current.db
    db.connect()

    # Log the query
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('web2py')
    logger.debug("Executing SQL: %s", query)

    # Execute the query
    raw_data = db.executesql(query, as_dict=True)

    return raw_data

# Usage
data = execute_query()
