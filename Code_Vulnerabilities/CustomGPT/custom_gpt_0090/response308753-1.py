
from gluon import current

def fetch_data():
    db = current.db
    query = """
        SELECT TIMESTAMPDIFF(...) AS 'duration',
               ris.ODATE as 'date',
               CONCAT(...) as 'service'
        FROM ... AS ris
        JOIN ... AS sd ON ris.... = sd....
        WHERE ris.... != '0000-00-00 00:00:00'
          AND ris.... >= '2010-8-15'
          AND ris.... <= '2014-8-22'
    """

    # Using connection pooling
    with db.connection:
        raw_data = db.executesql(query, as_dict=True)

    return raw_data
