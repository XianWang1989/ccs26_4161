
import pandas as pd

# Sample DataFrame
data = {
    'reader': [1, None, 3, 4, None],
    'other_column': ['A', 'B', 'C', 'D', 'E']
}
apps = pd.DataFrame(data)

# Boolean Series to filter rows
group_indexes = pd.Series([True, False, True, False, True])

# Filtering using group_indexes and checking not null in 'reader' column
result = apps[group_indexes]['reader'].notnull()

print(result)
