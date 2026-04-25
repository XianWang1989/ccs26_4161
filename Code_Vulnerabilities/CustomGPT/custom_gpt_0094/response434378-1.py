
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader2', None, 'Reader4']
}
apps = pd.DataFrame(data)

# Boolean Series for indexing
group_indexes = pd.Series([True, False, True, False])

# Filtering and checking for non-null values in the 'reader' column
non_null_readers = apps[group_indexes]['reader'].notnull()

print(non_null_readers)
