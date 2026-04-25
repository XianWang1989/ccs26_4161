
import pandas as pd

# Sample DataFrame
data = {
    'app': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader1', None, 'Reader2']
}
apps = pd.DataFrame(data)

# Boolean Series for filtering
group_indexes = pd.Series([True, False, True, True])

# Applying the boolean mask and checking for non-null values
non_null_readers = apps[group_indexes]['reader'].notnull()

print(non_null_readers)
