
# Import necessary libraries
from gluon import current, redirect
from gluon.debug import dbg

# Establish database connection
dbs = current.db

# Your SQL query
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       TIMESTAMPDIFF(...) - INTERVAL 1 HOUR,
       ris.ODATE as 'date',
       CONCAT(...) as 'service'
FROM ... AS ris
JOIN ... as sd on ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
AND ris.... &gt;= '2010-8-15'
AND ris.... &lt;= '2014-8-22'
"""

# Timing the execution of the query
raw_data = dbs.executesql(query, as_dict=True)  # This could take time
print(dbs._timings)

# Debug mode to analyze performance
dbg.set_trace()  # Start the debugger here

# Execute again to see the time improvement in debug mode
raw_data = dbs.executesql(query, as_dict=True)  # Should be faster
print(dbs._timings)
