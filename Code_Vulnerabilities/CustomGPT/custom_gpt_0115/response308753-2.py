
query = "SELECT * FROM my_table WHERE my_column = %s"
params = ('value',)
raw_data = db.executesql(query, params)
