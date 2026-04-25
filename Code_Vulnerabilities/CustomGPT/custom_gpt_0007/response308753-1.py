
def get_raw_data():
    query = "SELECT TIMESTAMPDIFF(...) AS 'duration', ... WHERE ris...."
    raw_data = dbs.executesql(query, as_dict=True)
    return raw_data
