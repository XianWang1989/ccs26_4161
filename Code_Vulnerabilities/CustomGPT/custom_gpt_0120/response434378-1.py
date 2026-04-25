
import pandas as pd

# Sample DataFrame
data = {
    'reader': [None, 'Alice', 'Bob', None, 'Charlie'],
    'other_column': [1, 2, 3, 4, 5]
}
apps = pd.DataFrame(data)

# Define a boolean index
group_indexes = pd.Series([True, False, True, False, True])

# Filtering the DataFrame and checking not null in the 'reader' column
result = apps[group_indexes]['reader'].notnull()

print(result)
