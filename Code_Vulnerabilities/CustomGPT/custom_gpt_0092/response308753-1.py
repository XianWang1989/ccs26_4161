
# models/db.py

# Ensure you have connection pooling enabled
db = DAL('mysql://username:password@localhost/dbname', pool_size=10)

# Example of executing a query with considerations for performance
def optimized_query():
    query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           TIMESTAMPDIFF(...) - INTERVAL 1 HOUR, 
           TIMESTAMP(...) + INTERVAL CAST(...) AS 'timediff',
           ris.ODATE as 'date',
           CONCAT(...) as 'service'
    FROM ... AS ris
    JOIN ... as sd ON ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
          AND ris.... != '0000-00-00 00:00:00'
          AND ris.... >= '2010-8-15'
          AND ris.... <= '2014-8-22'
    """

    # Begin transaction for better performance
    with db.transaction():
        raw_data = db.executesql(query, as_dict=True)

    return raw_data

# Example usage in a controller
def my_controller():
    data = optimized_query()
    return dict(data=data)
