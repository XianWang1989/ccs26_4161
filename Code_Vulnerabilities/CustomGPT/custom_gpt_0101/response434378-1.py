
import pandas as pd

# Sample DataFrame
data = {
    'reader': [1, 2, None, 4, None],
    'other_column': ['a', 'b', 'c', 'd', 'e']
}
apps = pd.DataFrame(data)

# Example boolean Series
group_indexes = pd.Series([True, False, True, False, True])

# Using group_indexes to filter the 'reader' column
filtered_not_null = apps[group_indexes]['reader'].notnull()

print(filtered_not_null)
