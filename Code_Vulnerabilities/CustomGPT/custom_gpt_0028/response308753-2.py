
import time

def execute_query(query):
    start_time = time.time()
    raw_data = db.executesql(query, as_dict=True)
    end_time = time.time()
    print(f"Query executed in: {end_time - start_time:.2f} seconds")
    return raw_data

# Sample query
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
    ris.ODATE as 'date',
    CONCAT(...) as 'service'
    FROM ... AS ris
    JOIN ... as sd on ris... = sd...
    WHERE ris... != '0000-00-00 00:00:00'
    AND ris... >= '2010-8-15'
    AND ris... <= '2014-8-22'
"""

# Execute query
execute_query(query)
