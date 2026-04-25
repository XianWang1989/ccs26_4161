
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App A', 'App B', 'App C', 'App D'],
    'reader': ['Reader 1', None, 'Reader 3', 'Reader 4']
}
apps = pd.DataFrame(data)

# Creating a boolean Series
group_indexes = pd.Series([True, False, True, True])

# Using boolean indexing to filter and check the 'reader' column for non-null values
not_null_readers = apps[group_indexes]['reader'].notnull()

# Displaying the results
print("Original DataFrame:")
print(apps)
print("\nBoolean Series (group_indexes):")
print(group_indexes)
print("\nNon-null values in 'reader' column after filtering:")
print(not_null_readers)
