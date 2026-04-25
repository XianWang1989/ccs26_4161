
def fetch_data():
    from gluon import current
    db = current.db

    query = """SELECT ..."""  # Replace with your SQL query

    # Logging execution time
    start_time = time.time()

    with db.connection:
        raw_data = db.executesql(query, as_dict=True)

    execution_time = time.time() - start_time
    print(f"Query executed in: {execution_time:.2f} seconds")

    return raw_data
