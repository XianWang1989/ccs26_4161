
queries = [
    "SELECT ...",
    "SELECT ...",
]
for q in queries:
    raw_data = db.executesql(q, as_dict=True)
