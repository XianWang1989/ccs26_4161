
with dbs.transaction():
    raw_data1 = dbs.executesql(query1, as_dict=True)
    raw_data2 = dbs.executesql(query2, as_dict=True)
