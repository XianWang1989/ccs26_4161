
import pandas as pd

# Sample DataFrame
data = {
    'reader': [None, 'Alice', 'Bob', None, 'Charlie'],
    'category': ['A', 'B', 'A', 'B', 'A']
}
apps = pd.DataFrame(data)

# Create a boolean Series (group_indexes) indicating which rows to filter
group_indexes = pd.Series([True, False, True, False, True])

# Use the boolean index to filter the DataFrame and then access the 'reader' column
not_null_readers = apps[group_indexes]['reader'].notnull()

# Display the result
print(not_null_readers)
