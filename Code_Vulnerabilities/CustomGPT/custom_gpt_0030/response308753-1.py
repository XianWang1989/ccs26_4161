
def fetch_data():
    # Example query with parameterized inputs
    query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           TIMESTAMPDIFF(...) - INTERVAL 1 HOUR, TIMESTAMP(...) + INTERVAL CAST(...) AS 'timediff',
           ris.ODATE as 'date',
           CONCAT(...) as 'service'
    FROM ... AS ris
    JOIN ... as sd on ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
    AND ris.... != '0000-00-00 00:00:00'
    AND ris.... >= %s
    AND ris.... <= %s
    """

    # Define parameters for date range
    params = ('2010-08-15', '2014-08-22')

    # Using a context manager for connection handling
    with db.connection.cursor() as cursor:
        # Execute query
        cursor.execute(query, params)
        raw_data = cursor.fetchall()

    return raw_data

# Usage
data = fetch_data()
print(data)
