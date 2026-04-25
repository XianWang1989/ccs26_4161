
# Ensure you have proper database connection settings
db = DAL('mysql://username:password@host/dbname', pool_size=10, migrate=True)

# Example function executing a query
def execute_query():
    query = """
        SELECT TIMESTAMPDIFF(...) AS duration, ris.ODATE AS date, CONCAT(...) AS service
        FROM ... AS ris
        JOIN ... AS sd ON ris.... = sd....
        WHERE ris.... != '0000-00-00 00:00:00'
        AND ris.... >= '2010-08-15'
        AND ris.... <= '2014-08-22'
    """

    # Use the with statement to maintain the connection
    with db.connection() as conn:
        raw_data = conn.executesql(query, as_dict=True)

    return raw_data
