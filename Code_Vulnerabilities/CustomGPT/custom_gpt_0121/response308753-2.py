
from gluon import current

# Example function to execute the query
def execute_query(query):
    db = current.db
    try:
        db.connect()  # Explicitly connect
        raw_data = db.executesql(query, as_dict=True)
    finally:
        db.close()  # Ensure connection is closed
    return raw_data
