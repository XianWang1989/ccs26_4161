
from gluon import current

# Establish database connection before executing queries
db = current.db
db.connect()

# Set session variables for performance
db.executesql("SET SESSION sql_mode='NO_BACKSLASH_ESCAPES';")

# Long-running query
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       ...  -- Additional logic here
FROM your_table AS ris
JOIN other_table AS sd ON ris.column = sd.column
WHERE ris.column != '0000-00-00 00:00:00'
AND ris.column BETWEEN '2010-08-15' AND '2014-08-22';
"""

# Benchmark execution time
import time

start_time = time.time()
raw_data = db.executesql(query, as_dict=True)
duration = time.time() - start_time
print(f"Query executed in {duration} seconds.")
