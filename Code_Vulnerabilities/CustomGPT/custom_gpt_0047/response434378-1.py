
import pandas as pd

# Sample DataFrame
data = {
    'reader': [1, None, 3, 4, None],
    'other_column': ['A', 'B', 'C', 'D', 'E']
}
apps = pd.DataFrame(data)

# Boolean Series to filter rows
group_indexes = apps['other_column'].isin(['A', 'C', 'D'])  # True for rows 0, 2, 3

# Apply the filter and check for non-null in 'reader'
result = apps[group_indexes]['reader'].notnull()

print(result)
