
from gluon import current

def run_query(query):
    db = current.db

    # Close and connect to ensure fresh state
    db.close()
    db.connect()

    try:
        # Measure execution time
        import time
        start_time = time.time()

        raw_data = db.executesql(query, as_dict=True)

        end_time = time.time()
        print(f"Query executed in {end_time - start_time:.2f} seconds")

        return raw_data
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()  # Ensure connection is closed afterward
