
from gluon import current
import time

def run_query():
    db = current.db
    if not db.connection:
        db.connect()

    query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration',
           TIMESTAMPDIFF(...) - INTERVAL 1 HOUR, TIMESTAMP(...)
    FROM ... AS ris
    WHERE ris.ODATE >= '2010-8-15' AND ris.ODATE <= '2014-8-22'
    """

    start_time = time.time()
    try:
        with db.transaction():
            raw_data = db.executesql(query, as_dict=True)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        end_time = time.time()
        print(f"Query executed in {end_time - start_time:.2f} seconds")

run_query()
