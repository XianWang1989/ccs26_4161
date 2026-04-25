
query = """
SELECT ...; -- Your SQL here 
SELECT ...; -- Another SQL
"""
raw_data = db.executesql(query, as_dict=True)
