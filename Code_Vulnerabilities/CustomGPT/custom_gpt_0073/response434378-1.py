
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader1', 'Reader2', None]
}
apps = pd.DataFrame(data)

# Sample boolean Series
group_indexes = pd.Series([False, True, True, False])

# Using the boolean indexing and accessing the 'reader' column
non_null_readers = apps[group_indexes]['reader'].notnull()

print(non_null_readers)
