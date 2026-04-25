
query = "SELECT * FROM table WHERE column = %s"
raw_data = db.executesql(query, (value,), as_dict=True)
