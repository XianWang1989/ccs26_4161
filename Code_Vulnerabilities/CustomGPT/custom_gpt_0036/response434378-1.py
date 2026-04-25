
import pandas as pd

# Sample data
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader1', None, 'Reader2']
}
apps = pd.DataFrame(data)

# Boolean Series for indexing
group_indexes = pd.Series([True, False, True, False])  # We want to only keep rows 0 and 2

# Filtering the DataFrame and checking for non-null values in the 'reader' column
result = apps[group_indexes]['reader'].notnull()

print(result)
