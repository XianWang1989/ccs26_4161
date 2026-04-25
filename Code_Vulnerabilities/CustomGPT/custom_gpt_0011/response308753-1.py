
# Assuming you have a variable `db` to access your database
from gluon import current

def get_optimized_data(query):
    db = current.db
    try:
        # Using a context manager to ensure proper connection usage
        with db.connection() as conn:
            # Execute the SQL query
            raw_data = db.executesql(query, as_dict=True)
            return raw_data
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

# Example usage
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           TIMESTAMPDIFF(...) - INTERVAL 1 HOUR,
           ris.ODATE AS 'date',
           CONCAT(...) AS 'service'
    FROM ... AS ris
    JOIN ... AS sd ON ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
    AND ris.... >= '2010-8-15'
    AND ris.... <= '2014-8-22'
"""
data = get_optimized_data(query)
print(data)
