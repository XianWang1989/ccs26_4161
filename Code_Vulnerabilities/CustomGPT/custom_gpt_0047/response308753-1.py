
def get_data():
    # Ensure you are using the same database connection
    db = current.db
    query = """SELECT TIMESTAMPDIFF(...) AS 'duration',
                       ris.ODATE as 'date',
                       CONCAT(...) as 'service'
                FROM ... AS ris
                JOIN ... as sd ON ris.... = sd....
                WHERE ris.... != '0000-00-00 00:00:00'
                  AND ris.... >= '2010-8-15'
                  AND ris.... <= '2014-8-22'"""

    # Using a context manager to ensure connections are reused properly
    with db.connection as conn:
        raw_data = conn.executesql(query, as_dict=True)

    return raw_data
