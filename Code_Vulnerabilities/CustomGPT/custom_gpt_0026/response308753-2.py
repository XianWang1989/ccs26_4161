
query = """SELECT ..."""  # Your SQL query

# Before executing the query
db._timings.clear()  
raw_data = db.executesql(query, as_dict=True)  
print(db._timings)  # Check timings after query execution
