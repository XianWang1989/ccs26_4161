
from gluon import current, SQLFORM

def execute_query():
    # Assuming you have a database connection object named 'dbs'
    query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           TIMESTAMPDIFF(...) - INTERVAL 1 HOUR, TIMESTAMP(...)
    FROM ... AS ris
    JOIN ... AS sd ON ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
          AND ris.... >= '2010-8-15'
          AND ris.... <= '2014-8-22'
    """

    # Timing the execution
    import time
    start_time = time.time()
    raw_data = dbs.executesql(query, as_dict=True)
    elapsed_time = time.time() - start_time

    return raw_data, elapsed_time

# Usage
data, duration = execute_query()
print(f"Query duration: {duration} seconds")
