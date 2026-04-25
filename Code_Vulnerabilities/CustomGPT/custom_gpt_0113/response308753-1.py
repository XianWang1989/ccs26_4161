
# Import necessary modules
from gluon import current, redirect
from gluon.debug import dbg

def my_view_function():
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

    # Using a raw connection
    db = current.db
    db.connect()

    try:
        # Execute query and measure time
        raw_data = db.executesql(query, as_dict=True)
        print(raw_data)
    finally:
        # Close the database connection
        db.close()
