
from gluon import current

# Define your query
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       ...
FROM your_table AS ris
JOIN another_table AS sd ON ris.id = sd.id
WHERE ris.created_at >= '2010-08-15'
  AND ris.created_at <= '2014-08-22'
  AND ris.other_condition != '0000-00-00 00:00:00'
"""

# Using executesql with context management
with current.db as db:
    try:
        # Run the query and measure execution time
        raw_data = db.executesql(query, as_dict=True)
    except Exception as e:
        print(f"Error executing query: {e}")
