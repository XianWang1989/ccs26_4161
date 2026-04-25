
from gluon import current
import time

def execute_query(query):
    db = current.db
    start_time = time.time()

    # Executing the raw SQL query
    result = db.executesql(query, as_dict=True)

    execution_time = time.time() - start_time
    current.response.flash = "Query executed in {:.2f} seconds".format(execution_time)

    # Logging the timings for analysis
    print("Query: {}\nExecution Time: {:.6f} seconds".format(query, execution_time))
    return result

# Example usage
if __name__ == "__main__":
    query = "SELECT TIMESTAMPDIFF(...) AS duration, ris.ODATE as date, CONCAT(...) as service FROM ... AS ris JOIN ... AS sd on ris.... = sd.... WHERE ris.... != '0000-00-00 00:00:00' AND ris.... >= '2010-8-15' AND ris.... <= '2014-8-22'"
    data = execute_query(query)
