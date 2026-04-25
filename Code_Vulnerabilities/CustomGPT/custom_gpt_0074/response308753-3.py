
from gluon import DAL

# Initialize the database connection with pooling enabled
db = DAL('mysql://username:password@localhost/mydatabase', pool_size=10)

# Example of running a potentially slow query
try:
    raw_data = db.executesql("""
        SELECT TIMESTAMPDIFF(...) AS 'duration',
               TIMESTAMPDIFF(...) - INTERVAL 1 HOUR, TIMESTAMP(...) + INTERVAL CAST(...) AS 'timediff',
               ris.ODATE as 'date',
               CONCAT(...) as 'service'
        FROM ... AS ris
        JOIN ... as sd on ris.... = sd....
        WHERE ris.... != '0000-00-00 00:00:00'
        AND ris.... != '0000-00-00 00:00:00'
        AND ris.... >= '2010-8-15'
        AND ris.... <= '2014-8-22';
    """, as_dict=True)
except Exception as e:
    print(f"An error occurred: {e}")
