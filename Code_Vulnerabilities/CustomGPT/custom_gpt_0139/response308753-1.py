
from gluon import current, redirect
import time

def execute_query(query):
    # Get the database instance
    db = current.dbs
    # Measure start time
    start_time = time.time()

    # Try to execute the query
    try:
        # Use executesql and return as dictionary
        result = db.executesql(query, as_dict=True)
    except Exception as e:
        # Handle any exception
        current.logger.error(f'Query failed: {e}')
        return None
    finally:
        # Measure end time
        duration = time.time() - start_time
        current.logger.info(f'Query executed in {duration:.4f} seconds')

    return result

def my_view():
    query = "SELECT TIMESTAMPDIFF(...) AS 'duration', ... FROM ..."
    raw_data = execute_query(query)

    if raw_data is not None:
        # Process and return your data as needed
        return dict(data=raw_data)
    else:
        # Handle the case where there is no data
        return dict(data=[])

