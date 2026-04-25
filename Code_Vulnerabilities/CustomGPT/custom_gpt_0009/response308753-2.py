
from gluon.debug import dbg

# Start debugging
dbg.set_trace() 
raw_data = dbs.executesql(query, as_dict=True)  # This should have faster execution
