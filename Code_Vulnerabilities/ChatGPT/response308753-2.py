
query = "SELECT * FROM your_table WHERE column = %s"
params = ('value',)

raw_data = dbs.executesql(query, params)
