
# Run queries without debug mode
if not request.is_debug:
    db._adapter._debug = False
raw_data = db.executesql(query, as_dict=True)
