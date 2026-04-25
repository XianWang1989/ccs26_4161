
# Warm up query
db.executesql("SELECT 1;")

# Your main query
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration', 
           TIMESTAMPDIFF(...) 
           - INTERVAL 1 HOUR, 
           TIMESTAMP(...) 
           + INTERVAL CAST(...) AS 'timediff', 
           ris.ODATE as 'date',
           CONCAT(...) as 'service' 
    FROM ... AS ris 
    JOIN ... as sd on ris.... = sd.... 
    WHERE ris.... != '0000-00-00 00:00:00'
          AND ris.... &gt;= '2010-8-15' 
          AND ris.... &lt;= '2014-8-22'
"""

# Execute
raw_data = db.executesql(query, as_dict=True)
