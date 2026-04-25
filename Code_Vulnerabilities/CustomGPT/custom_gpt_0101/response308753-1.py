
# Sample code to demonstrate the issue with db.executesql in web2py

# Assume `dbs` is your database connection

query = """
SELECT TIMESTAMPDIFF(SQL_BETWEEN_COLUMNS)
AS 'duration',
...
FROM ...
JOIN ...
WHERE ...
"""

# Execution taking too long in web2py
raw_data = dbs.executesql(query, as_dict=True)  # Expected long execution time

# Debugging to check execution time
from gluon.debug import dbg
dbg.set_trace()

# Re-running the same query in debug console for performance comparison
raw_data = dbs.executesql(query, as_dict=True)  # Expected a much faster execution time
