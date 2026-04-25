
from gluon import current
from gluon.dal import DAL

# Example of adjusting db connection settings
db = DAL('mysql://user:password@localhost/dbname', pool_size=1)

def run_query():
    try:
        # Start timing
        import time
        start_time = time.time()

        # Perform query
        raw_data = db.executesql('SELECT * FROM SomeTable WHERE condition', as_dict=True)

        # Print elapsed time
        elapsed_time = time.time() - start_time
        print(f"Query executed in: {elapsed_time:.2f} seconds")

    except Exception as e:
        print(f"An error occurred: {e}")

run_query()
