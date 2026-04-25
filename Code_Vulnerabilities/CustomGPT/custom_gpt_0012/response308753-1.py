
from gluon.globals import current

# Ensure persistent connection
if current.db._uri:
    current.db._adapter._persistent = True

# Your SQL query
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration', ...
    FROM ... AS ris
    JOIN ... as sd on ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
    AND ris.... != '0000-00-00 00:00:00'
    AND ris.... >= '2010-8-15'
    AND ris.... <= '2014-8-22'
"""

# Execute the SQL query
raw_data = current.db.executesql(query, as_dict=True)
