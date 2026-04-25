
# Warm up the database connection
db.executesql("SELECT 1;")
raw_data = db.executesql(query, as_dict=True)  # Your actual query
