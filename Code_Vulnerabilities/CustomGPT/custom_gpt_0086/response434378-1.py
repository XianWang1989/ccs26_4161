
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader1', None, 'Reader2'],
}

apps = pd.DataFrame(data)

# Boolean Series indicating which rows to include
group_indexes = pd.Series([True, False, True, False])

# Filtering and checking for not null
not_null_readers = apps[group_indexes]['reader'].notnull()

print(not_null_readers)
