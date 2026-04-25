
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader2', None, 'Reader4']
}
apps = pd.DataFrame(data)

# Sample boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])

# Filtering and accessing the 'reader' column
filtered_readers = apps[group_indexes]['reader']

# Checking for non-null values in the filtered 'reader' column
non_null_readers = filtered_readers.notnull()

print(non_null_readers)
