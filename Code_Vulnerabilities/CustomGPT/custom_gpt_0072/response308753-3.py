
queries = [
    "SELECT TIMESTAMPDIFF(...) AS 'duration' FROM ...;",
    "SELECT ...;"
]
for q in queries:
    db.executesql(q)
