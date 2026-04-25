
# Combine multiple queries into a single call if possible
query = """
SELECT * FROM table1;
SELECT * FROM table2;
"""
results = db.executesql(query)
