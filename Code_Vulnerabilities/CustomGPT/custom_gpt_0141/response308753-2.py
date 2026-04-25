
from gluon import *

# Initialize the database with connection pooling
db = DAL('mysql://username:password@host/database', pool_size=10)

def execute_query():
    query = """
        SELECT TIMESTAMPDIFF(...), ris.ODATE as 'date', CONCAT(...) as 'service'
        FROM ... AS ris
        JOIN ... AS sd on ris.... = sd....
        WHERE ris.... != '0000-00-00 00:00:00'
        AND ris.... != '0000-00-00 00:00:00'
        AND ris.... >= '2010-8-15'
        AND ris.... <= '2014-8-22'
    """

    # Execute the query and measure time
    import time
    start_time = time.time()

    raw_data = db.executesql(query, as_dict=True)

    # Print the execution time
    execution_time = time.time() - start_time
    print("Execution Time:", execution_time, "seconds")

    return raw_data

# Usage
if __name__ == "__main__":
    data = execute_query()
    print(data)
