
from gluon.debug import dbg
dbg.set_trace()  # Check if there are uninitialized variables affecting speed

# Execute the same query for performance comparison
raw_data = dbs.executesql(query, as_dict=True)
