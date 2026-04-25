
from gluon import current

def execute_query(query, params=None):
    # Set the query cache type
    current.db.executesql("SET SESSION query_cache_type = 1;")

    # Use params to prevent SQL injection and optimize performance
    if params:
        raw_data = current.db.executesql(query, params, as_dict=True)
    else:
        raw_data = current.db.executesql(query, as_dict=True)

    return raw_data

# Example usage
query = "SELECT * FROM your_table WHERE some_column = %s"
params = (some_value,)
data = execute_query(query, params)
