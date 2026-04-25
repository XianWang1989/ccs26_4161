
import time

def execute_query(query):
    start_time = time.time()
    try:
        raw_data = db.executesql(query, as_dict=True)
    except Exception as e:
        return {'error': str(e)}
    finally:
        elapsed_time = time.time() - start_time
        print(f"Query executed in {elapsed_time:.2f} seconds")
    return raw_data

# Example usage
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       ris.ODATE as 'date',
       CONCAT(...) as 'service'
FROM ... AS ris
JOIN ... AS sd ON ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00'
AND ris.... >= '2010-08-15'
AND ris.... <= '2014-08-22'
"""

results = execute_query(query)
print(results)
