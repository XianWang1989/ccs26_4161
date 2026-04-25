
query = "SELECT * FROM my_table WHERE id = %s"
raw_data = db.executesql(query, (some_id,), as_dict=True)
