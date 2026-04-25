
queries = [
    "SELECT * FROM table1 WHERE conditions;",
    "SELECT * FROM table2 WHERE conditions;"
]
for query in queries:
    dbs.executesql(query)
