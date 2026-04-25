
import pandas as pd

# Sample DataFrame
data = {
    'app': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader1', 'Reader2', None]
}

apps = pd.DataFrame(data)

# Boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])

# Filtering and checking for non-null values in the 'reader' column
non_null_readers = apps[group_indexes]['reader'].notnull()

print(non_null_readers)
