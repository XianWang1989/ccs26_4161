
for i in range(5):  # Execute the query multiple times
    start_time = time.time()
    raw_data = db.executesql(query, as_dict=True)
    execution_time = time.time() - start_time
    print(f"Execution time for iteration {i + 1}: {execution_time} seconds")
