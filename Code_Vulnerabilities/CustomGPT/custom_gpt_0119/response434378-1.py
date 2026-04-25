
import pandas as pd

# Sample DataFrame
data = {
    'reader': [1, None, 3, None, 5],
    'other_column': ['A', 'B', 'C', 'D', 'E']
}
apps = pd.DataFrame(data)

# Boolean Series for indexing
group_indexes = pd.Series([True, False, True, False, True])

# Filter 'reader' column for not null values based on group_indexes
result = apps[group_indexes]['reader'].notnull()

print(result)
