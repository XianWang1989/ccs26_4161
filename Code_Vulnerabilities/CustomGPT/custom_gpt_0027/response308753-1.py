
import time

# Sample SQL query
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration', 
           ris.ODATE as 'date', 
           CONCAT(...) as 'service'
    FROM ... AS ris
    JOIN ... as sd ON ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
          AND ris.... >= '2010-8-15'
          AND ris.... <= '2014-8-22'
"""

# Timing the execution
start_time = time.time()
raw_data = dbs.executesql(query, as_dict=True)
end_time = time.time()

print(f"Execution Time: {end_time - start_time:.2f} seconds")
