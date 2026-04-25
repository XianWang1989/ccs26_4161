
def run_queries():
    db = DAL('mysql://user:password@host/dbname', pool_size=10)

    # Optimized SQL query
    query = """SELECT TIMESTAMPDIFF(...) AS duration, ... FROM ... WHERE ..."""

    # Clear existing timings
    db._timings.clear()

    # Execute and measure timing
    raw_data = db.executesql(query, as_dict=True)
    print("Query took: ", db._timings)

    # Further processing

# Call the function in the appropriate route
