
db._adapter._auto_commit = False  # Disable auto-committing
raw_data = db.executesql(query, as_dict=True)  # Test without caching
