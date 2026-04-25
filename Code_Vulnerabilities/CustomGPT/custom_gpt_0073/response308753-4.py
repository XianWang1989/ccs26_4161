
import time
from gluon import current

def fetch_data(start_date, end_date):
    db = current.db

    # Timing the query
    start_time = time.time()

    # Using parameterized query
    query = (db.ris.odate >= start_date) & (db.ris.odate <= end_date)
    raw_data = db(query).select(db.ris.odate, db.ris.service).as_list()

    end_time = time.time()
    print("Query executed in: {:.2f} seconds".format(end_time - start_time))

    return raw_data

# Call the function with dates
data = fetch_data('2010-08-15', '2014-08-22')
