
# Assuming 'dbs' is your database connection
from gluon import current

# Use connection pooling
current.db = current.globalenv['db']

# Sample query
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       TIMESTAMPDIFF(...) - INTERVAL 1 HOUR AS 'timediff',
       ris.ODATE as 'date',
       CONCAT(...) as 'service'
FROM ... AS ris
JOIN ... AS sd ON ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
  AND ris.... >= '2010-8-15'
  AND ris.... <= '2014-8-22'
"""

# Start profiling
current.db.executesql("SET profiling = 1;")

# Execute your query
raw_data = current.db.executesql(query, as_dict=True)

# Check profiling results
profiling_results = current.db.executesql("SHOW PROFILES;")
print(profiling_results)

# Do this in the web2py shell to compare timings
