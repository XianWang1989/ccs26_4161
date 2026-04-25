
from gluon import current
from gluon.debug import dbg

def fetch_data():
    db = current.db

    # Example SQL Query - ensure it's optimized
    query = '''
        SELECT TIMESTAMPDIFF(...), 
        ris.ODATE AS date, 
        CONCAT(...) AS service 
        FROM ... AS ris 
        JOIN ... AS sd ON ris... = sd... 
        WHERE ris... != '0000-00-00 00:00:00' 
        AND ris... >= '2010-8-15' 
        AND ris... <= '2014-8-22'
    '''

    # First execution to demonstrate performance issue
    raw_data = db.executesql(query, as_dict=True)  # Measure performance
    print("Time taken for query (first attempt):", db._timings[-1][1])

    # Debugging step to compare performance
    dbg.set_trace()

    # Running the same query in debug console
    raw_data = db.executesql(query, as_dict=True)  # Should be faster
    print("Time taken for query (after debug):", db._timings[-1][1])

    return raw_data

data = fetch_data()
# Process or return fetched data as needed
