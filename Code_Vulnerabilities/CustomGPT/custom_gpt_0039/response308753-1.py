
# Ensure you import web2py's database features
from gluon import DAL

# Initialize your database
db = DAL('mysql://user:password@host/dbname', pool_size=10, check_reserved=['all'])

# Your SQL query
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           TIMESTAMPDIFF(...) - INTERVAL 1 HOUR, TIMESTAMP(...) + INTERVAL CAST(...) AS 'timediff',
           ris.ODATE as 'date',
           CONCAT(...) as 'service'
    FROM ... AS ris
    JOIN ... as sd on ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
          AND ris.... >= '2010-8-15'
          AND ris.... <= '2014-8-22'
"""

# Example function to run the query
def run_query():
    # Use context management for persistent connections
    with db.connection:
        raw_data = db.executesql(query, as_dict=True)
    return raw_data

# Call the function and measure time
import time
start_time = time.time()
result = run_query()
end_time = time.time()
print(f"Query executed in {end_time - start_time} seconds")
