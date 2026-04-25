
def execute_query(query):
    import time

    # Start timing
    start_time = time.time()

    try:
        # Execute SQL query
        raw_data = db.executesql(query, as_dict=True)
    except Exception as e:
        return {"error": str(e)}

    # End timing
    duration = time.time() - start_time

    # Return the data and the execution time
    return {
        "data": raw_data,
        "execution_time": duration
    }

# Sample usage
if __name__ == "__main__":
    query = """
        SELECT TIMESTAMPDIFF(...) AS 'duration',
        ... -- Rest of your query
    """

    result = execute_query(query)
    print(result["execution_time"])  # Check how long it took
