
# Ensure you are using the correct database and settings
from gluon import current

# Optimize your connection settings
db = current.db

# Provide an explicit connection timeout
db._uri = 'mysql://username:password@host:port/dbname?charset=utf8&connect_timeout=2'
db._adapter = 'mysql'

# Run your SQL query
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration', ...
    FROM ... AS ris
    JOIN ... AS sd ON ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
      AND ris.... >= '2010-8-15'
      AND ris.... <= '2014-8-22'
"""
raw_data = db.executesql(query, as_dict=True)
