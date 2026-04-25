
# Example of managing the database connection
def run_query(dbs, query):
    dbs.connect()  # Explicitly connect to the database
    try:
        raw_data = dbs.executesql(query, as_dict=True)
    finally:
        dbs.close()  # Ensure connection is closed
    return raw_data
