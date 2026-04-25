
def execute_query_directly(query):
    db = current.db
    result = db._adapter.query(query)  # Directly query using the adapter
    return result.fetchall()  # Fetch results
