
from gluon import DAL, Field

# Setup database connection
db = DAL('mysql://user:password@host/dbname', pool_size=10, migrate=True)

def get_data(query):
    try:
        raw_data = db.executesql(query, as_dict=True)
        return raw_data
    except Exception as e:
        print(f"Error executing query: {e}")

# Example query
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           TIMESTAMPDIFF(...) - INTERVAL 1 HOUR,
           ris.ODATE as 'date',
           CONCAT(...) as 'service'
    FROM ... AS ris
    JOIN ... as sd on ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
      AND ris.... >= '2010-8-15'
      AND ris.... <= '2014-8-22'
"""

# Call function
results = get_data(query)
print(results)
