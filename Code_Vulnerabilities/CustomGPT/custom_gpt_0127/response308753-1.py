
from gluon import *
from gluon.debug import dbg

# Sample query
query = """
SELECT ...
FROM ...
WHERE ...
"""

# Example of executing a query
try:
    # Ensure to use a context manager if possible
    with db.transaction():
        # First execution (may be slow)
        raw_data = db.executesql(query, as_dict=True)

    # Debugging point
    dbg.set_trace()

    # Subsequent executions (should be faster)
    for _ in range(3):
        raw_data = db.executesql(query, as_dict=True)

except Exception as e:
    print(f"An error occurred: {e}")

# Check timings
timings = db._timings
print(timings)
