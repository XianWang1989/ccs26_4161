
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader1', 'Reader2', None],
    'rating': [4.2, 5.0, 3.5, 4.8]
}

apps = pd.DataFrame(data)

# Boolean Series to filter apps
group_indexes = apps['rating'] > 4.0

# Filtered 'reader' column for non-null values
non_null_readers = apps[group_indexes]['reader'].notnull()

print(non_null_readers)
