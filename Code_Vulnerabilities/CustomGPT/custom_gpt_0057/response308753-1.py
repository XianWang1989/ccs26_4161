
from gluon import DAL, current

database_uri = 'mysql://user:password@localhost/dbname'
db = DAL(database_uri, pool_size=10, wait_timeout=60)

def execute_query(query):
    try:
        raw_data = db.executesql(query, as_dict=True)
        print(f"Query executed successfully: {raw_data}")
    except Exception as e:
        print(f"Error executing query: {str(e)}")

query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
TIMESTAMPDIFF(...)
- INTERVAL 1 HOUR, TIMESTAMP(...)
+ INTERVAL CAST(...) AS 'timediff',
ris.ODATE as 'date',
CONCAT(...) as 'service'
FROM ... AS ris
JOIN ... as sd on ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
AND ris.... != '0000-00-00 00:00:00'
AND ris.... >= '2010-8-15'
AND ris.... <= '2014-8-22'
"""

execute_query(query)
