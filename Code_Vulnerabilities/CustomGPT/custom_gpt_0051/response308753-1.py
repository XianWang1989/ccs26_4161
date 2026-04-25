
import time

def run_queries():
    with db.connection() as conn:
        # Ensure you're using the same connection
        start_time = time.time()
        query = """
        SELECT TIMESTAMPDIFF(...) AS 'duration',
               ris.ODATE as 'date',
               CONCAT(...) as 'service'
        FROM ... AS ris
        JOIN ... as sd ON ...
        WHERE ris.... >= '2010-8-15'
          AND ris.... <= '2014-8-22'
          AND ris.... != '0000-00-00 00:00:00'
        """

        # First execution
        raw_data = conn.executesql(query, as_dict=True)
        print(f"First query execution time: {time.time() - start_time} seconds")

        # Subsequent executions
        for _ in range(2):
            start_time = time.time()
            raw_data = conn.executesql(query, as_dict=True)
            print(f"Subsequent query execution time: {time.time() - start_time} seconds")

# Call the function
run_queries()
