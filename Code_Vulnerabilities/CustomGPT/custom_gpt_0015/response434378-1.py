
import pandas as pd

# Sample DataFrame
data = {
    'reader': [1, None, 3, None, 5],
    'other_col': ['a', 'b', 'c', 'd', 'e']
}
apps = pd.DataFrame(data)

# Boolean Series indicating which rows to select
group_indexes = pd.Series([True, False, True, False, True])

# Using the boolean index to filter and check for non-null values
not_null_readers = apps[group_indexes]['reader'].notnull()

# Display the result
print(not_null_readers)
