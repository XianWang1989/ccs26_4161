
# Import necessary modules
from gluon import current
from gluon.debug import dbg

# Sample query
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       TIMESTAMPDIFF(...) - INTERVAL 1 HOUR,
       ris.ODATE as 'date',
       CONCAT(...) as 'service'
FROM ... AS ris
JOIN ... as sd on ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
AND ris.... >= '2010-08-15'
AND ris.... <= '2014-08-22'
"""

# Testing query execution times
def test_query_execution():
    db = current.db
    # Disable caching for testing purpose
    db.tables._cache = False

    # Execute the query
    raw_data = db.executesql(query, as_dict=True)
    print("First execution time: {} seconds".format(db._timings[-1][-1]))

    # Debug console point
    dbg.set_trace()

    # Execute again after debugger
    raw_data = db.executesql(query, as_dict=True)
    print("Second execution time: {} seconds".format(db._timings[-1][-1]))

# Call the test function
test_query_execution()
