
with db.transaction():
    raw_data1 = db.executesql(query1, as_dict=True)
    raw_data2 = db.executesql(query2, as_dict=True)
