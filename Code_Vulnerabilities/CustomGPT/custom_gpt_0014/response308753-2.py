
# Before executing the long-running query
dbs.executesql("SET SESSION sql_mode='NO_BACKSLASH_ESCAPES';")
raw_data = dbs.executesql(query, as_dict=True)  # Execute your query
