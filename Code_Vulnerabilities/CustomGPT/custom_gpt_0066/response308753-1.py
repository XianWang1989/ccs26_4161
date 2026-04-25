
from gluon import current

# Function to execute SQL safely and effectively
def execute_sql(query, as_dict=True):
    db = current.db
    try:
        # Optionally, use with statement to ensure proper connection management
        with db.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall() if not as_dict else [dict(row) for row in cursor.fetchall()]
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           ris.ODATE as 'date',
           CONCAT(...) as 'service'
    FROM ... AS ris
    JOIN ... AS sd ON ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
          AND ris.... >= '2010-08-15'
          AND ris.... <= '2014-08-22'
"""

# This should ideally execute with improved timing
raw_data = execute_sql(query, as_dict=True)
