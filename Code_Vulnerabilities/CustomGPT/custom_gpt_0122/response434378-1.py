
import pandas as pd

# Sample DataFrame
data = {
    'reader': [None, 'Book A', 'Book B', None, 'Book C'],
    'other_column': [1, 2, 3, 4, 5]
}
apps = pd.DataFrame(data)

# Boolean Series for indexing
group_indexes = pd.Series([True, False, True, False, True])

# Filtering and checking for non-null values in 'reader'
result = apps[group_indexes]['reader'].notnull()

print(result)
