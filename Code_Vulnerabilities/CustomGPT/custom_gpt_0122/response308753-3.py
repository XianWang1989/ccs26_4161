
query = "SELECT TIMESTAMPDIFF(...) AS 'duration' FROM ..."
raw_data = db.executesql(query, as_dict=True)
