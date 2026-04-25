
# Ensure you're using the right database connection settings in your model
import datetime

def get_data():
    # Use a context manager to ensure proper connection handling
    with db.connection as conn:
        # Your SQL query
        query = """
            SELECT TIMESTAMPDIFF(...), ris.ODATE as 'date', CONCAT(...) as 'service'
            FROM ... AS ris
            JOIN ... as sd ON ris.... = sd....
            WHERE ris.... != '0000-00-00 00:00:00'
              AND ris.... >= '2010-8-15'
              AND ris.... <= '2014-8-22'
        """
        # Execute the SQL query
        raw_data = conn.executesql(query, as_dict=True)
        return raw_data

result = get_data()
