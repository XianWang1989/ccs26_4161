
# In your web2py model (models/db.py)

from gluon import current

# Function to execute SQL with improved connection management
def run_query(query):
    db = current.db
    try:
        # Acquire connection from pool
        db.commit()  # Ensure previous commands are committed
        result = db.executesql(query, as_dict=True)
        return result
    except Exception as e:
        db.rollback()  # Rollback on error
        raise e

# Example use in a controller
def some_controller_function():
    query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           ris.ODATE as 'date',
           CONCAT(...) as 'service'
    FROM ... AS ris
    JOIN ... as sd ON ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
    AND ris.... >= '2010-8-15'
    AND ris.... <= '2014-8-22'
    """
    data = run_query(query)
    return dict(data=data)
