
import time
from gluon.debug import dbg

def execute_query(query):
    start_time = time.time()

    # Execute the query
    try:
        raw_data = db.executesql(query, as_dict=True)
    except Exception as e:
        print(f"Error executing query: {e}")
        raw_data = None

    elapsed_time = time.time() - start_time
    print(f"Query executed in: {elapsed_time:.2f} seconds")

    return raw_data

# Test the execution time in the web2py context
if __name__ == "__main__":
    dbs._timings.clear()  # Clear previous timings
    query = """SELECT TIMESTAMPDIFF(...) AS 'duration',
                       TIMESTAMPDIFF(...) - INTERVAL 1 HOUR,
                       TIMESTAMP(...) + INTERVAL CAST(...) AS 'timediff',
                       ris.ODATE as 'date', CONCAT(...) as 'service'
                FROM ... AS ris
                JOIN ... as sd ON ris.... = sd....
                WHERE ris.... != '0000-00-00 00:00:00'
                AND ris.... != '0000-00-00 00:00:00'
                AND ris.... >= '2010-8-15'
                AND ris.... <= '2014-8-22'"""

    raw_data = execute_query(query)

    # Debugging with the debugger - this line drops you into the debug console
    dbg.set_trace()

    # After hitting debugging, re-execute to see changes/improvements
    new_raw_data = execute_query(query)  # See if it runs faster now
