
# Ensure your database connection uses pooling
db = DAL('mysql://username:password@localhost/dbname', pool_size=10)

# Define your SQL query as a prepared statement
query = """
    SELECT TIMESTAMPDIFF(...), ris.ODATE as 'date', CONCAT(...) as 'service'
    FROM ... AS ris
    JOIN ... as sd on ris.... = sd....
    WHERE ris.... != '0000-00-00 00:00:00'
      AND ris.... >= %s
      AND ris.... <= %s
"""

# Use parameters to execute the query
start_time = time.time()
raw_data = db.executesql(query, ('2010-08-15', '2014-08-22'), as_dict=True)
print("Query Time:", time.time() - start_time)

# Check the timings
print(db._timings)
