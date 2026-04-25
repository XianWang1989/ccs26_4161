
with db.transaction():
    raw_data = db.executesql(query, as_dict=True)
