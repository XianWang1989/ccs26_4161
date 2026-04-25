
query = "SELECT ... FROM ... WHERE ..."
db.raw(query)  # You can also log the raw query for debugging
raw_data = db.executesql(query, as_dict=True)
