
# Assume `dbs` is defined and connects to the MySQL instance.

def execute_query(query, as_dict=True):
    # Log the start time
    import time
    start_time = time.time()

    # Attempt to execute the query
    try:
        raw_data = dbs.executesql(query, as_dict=as_dict)
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

    # Log the duration
    duration = time.time() - start_time
    print(f"Query executed in: {duration:.2f} seconds")

    return raw_data

# Sample query which can be replaced with original
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration',
       ris.ODATE as 'date',
       CONCAT(...) as 'service'
FROM ... AS ris
WHERE ris.... != '0000-00-00 00:00:00'
  AND ris.... >= '2010-8-15'
  AND ris.... <= '2014-8-22'
"""

# Execute the query
data = execute_query(query)
