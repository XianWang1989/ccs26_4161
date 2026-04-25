
def optimized_query():
    # Warm-up query to help cache the execution plan
    db.executesql("SELECT 1;")

    # Your main query
    query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           TIMESTAMPDIFF(...) - INTERVAL 1 HOUR,
           ris.ODATE as 'date',
           CONCAT(...) as 'service'
    FROM ... AS ris
    JOIN ... AS sd ON ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
      AND ris.... != '0000-00-00 00:00:00'
      AND ris.... >= '2010-08-15'
      AND ris.... <= '2014-08-22';
    """

    # Execute the main query
    raw_data = db.executesql(query, as_dict=True)
    return raw_data
