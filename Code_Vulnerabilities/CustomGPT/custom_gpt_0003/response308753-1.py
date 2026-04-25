
# Assuming db is your web2py database object
from gluon import current

# Example of using a connection pool efficiently
def get_data(dates):
    query = "SELECT TIMESTAMPDIFF(...) AS 'duration', ris.ODATE as 'date' FROM ... AS ris WHERE ris.ODATE BETWEEN %s AND %s;"
    results = []

    # Use context manager for transactions
    with current.db.connection as conn:
        cursor = conn.cursor()

        # Batch execution of multiple queries
        for date_range in dates:
            start_date, end_date = date_range
            cursor.execute(query, (start_date, end_date))
            results.append(cursor.fetchall())

        conn.commit()  # Explicitly committing if not using autocommit

    return results

# Define your date ranges
date_ranges = [('2010-08-15', '2014-08-22'), ('2010-08-16', '2014-08-23')]
data = get_data(date_ranges)

# Output the results
for entry in data:
    print(entry)
