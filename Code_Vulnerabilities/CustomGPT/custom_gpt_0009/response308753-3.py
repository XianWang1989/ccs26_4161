
queries = [
    "SELECT ...",  # first query
    "SELECT ..."   # second query
]

# Execute all in a single call if possible
results = dbs.executesql("; ".join(queries), as_dict=True)
