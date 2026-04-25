
# Example of executing a query with connection pooling and performance logging

def execute_query(dbs, query):
    # Start profiling
    import time
    start_time = time.time()

    try:
        # Using as_dict for easier handling of results
        raw_data = dbs.executesql(query, as_dict=True)
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

    elapsed_time = time.time() - start_time
    print(f"Query executed in: {elapsed_time:.2f} seconds")

    return raw_data

# Example usage
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration', ...
FROM ... AS ris
JOIN ... as sd ON ris.... = sd....
WHERE ris.... NOT IN ('0000-00-00 00:00:00')
AND ris.... >= '2010-08-15' AND ris.... <= '2014-08-22'
"""

# Execute the query
data = execute_query(dbs, query)
