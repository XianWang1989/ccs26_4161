
import pandas as pd

# Sample data
data = {
    'reader': [None, 'Alice', 'Bob', None, 'Charlie'],
    'other_column': [1, 2, 3, 4, 5]
}
apps = pd.DataFrame(data)

# Boolean index
group_indexes = pd.Series([True, False, True, False, True], index=apps.index)

# Applying boolean indexing
not_null_readers = apps[group_indexes]['reader'].notnull()

print(not_null_readers)
