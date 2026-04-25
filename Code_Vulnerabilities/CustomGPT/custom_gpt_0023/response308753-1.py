
from gluon import current, db
from gluon.debug import dbg

def optimized_query():
    query = """SELECT TIMESTAMPDIFF(...) AS 'duration',
                TIMESTAMPDIFF(...) - INTERVAL 1 HOUR,
                ris.ODATE AS 'date', CONCAT(...) AS 'service'
                FROM ... AS ris
                JOIN ... AS sd ON ris.... = sd....
                WHERE ris.... != '0000-00-00 00:00:00'
                  AND ris.... >= '2010-8-15'
                  AND ris.... <= '2014-8-22'"""

    # Begin a transaction
    db.transaction()
    try:
        raw_data = db.executesql(query, as_dict=True)
        # Process raw_data as needed
    finally:
        db.commit()  # Ensure the transaction is committed

# Validate performance
dbg.set_trace()  # Measure execution time here
optimized_query()
