
import logging
from gluon import current

# Configure logging
logging.basicConfig(level=logging.DEBUG, filename='query_log.txt', filemode='a')

def execute_query(query):
    db = current.db
    try:
        db.begin()  # Start transaction
        raw_data = db.executesql(query, as_dict=True)
        db.commit()  # Commit transaction
        logging.debug(f"Query executed: {query}, Result: {raw_data}")
        return raw_data
    except Exception as e:
        db.rollback()  # Rollback if there's an error
        logging.error(f"Error executing query: {query}, Error: {str(e)}")
        return None

# Usage
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           ris.ODATE as 'date',
           CONCAT(...) as 'service'
    FROM ... AS ris
    JOIN ... as sd on ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
    AND ris.... >= '2010-8-15'
    AND ris.... <= '2014-8-22'
"""

# Execute the query
raw_data = execute_query(query)
