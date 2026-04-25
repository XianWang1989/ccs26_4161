
from gluon import current

def execute_query(param1, param2):
    db = current.db
    query = """
        SELECT TIMESTAMPDIFF(...), ris.ODATE as 'date', CONCAT(...) as 'service'
        FROM ... AS ris
        JOIN ... as sd on ris.... = sd....
        WHERE ris.... != '0000-00-00 00:00:00'
        AND ris.... != '0000-00-00 00:00:00'
        AND ris.... >= %s
        AND ris.... <= %s
    """

    # Set a timeout for the query
    db.commit()  # To apply any previous changes
    db._adapter.query_timeout = 10  # Set timeout to 10 seconds

    raw_data = db.executesql(query, (param1, param2), as_dict=True)

    return raw_data

# Usage
start_date = '2010-08-15'
end_date = '2014-08-22'
data = execute_query(start_date, end_date)
