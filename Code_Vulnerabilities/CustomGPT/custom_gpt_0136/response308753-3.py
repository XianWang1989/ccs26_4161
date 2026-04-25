
explain_query = f"EXPLAIN {query}"
raw_data = db.executesql(explain_query)
print(raw_data)  # Analyze performance
