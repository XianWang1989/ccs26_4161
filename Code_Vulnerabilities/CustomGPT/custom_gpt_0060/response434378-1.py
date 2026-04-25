
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 150, 200, None]
}
apps = pd.DataFrame(data)

# Boolean Series: True if the app index is even, False if odd
group_indexes = pd.Series([True if i % 2 == 0 else False for i in range(len(apps))])

# Use the boolean mask to filter the 'reader' column
filtered_readers = apps[group_indexes]['reader']

# Check which values are not null
non_null_readers = filtered_readers.notnull()

# Display results
print("Original DataFrame:")
print(apps)
print("\nBoolean Indexes:")
print(group_indexes)
print("\nFiltered 'reader' values:")
print(filtered_readers)
print("\nNon-null 'reader' check:")
print(non_null_readers)
