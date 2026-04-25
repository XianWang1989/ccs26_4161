
import pandas as pd

# Sample data
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader1', None, 'Reader2'],
    'category': ['Utility', 'Utility', 'Game', 'Social']
}

# Create DataFrame
apps = pd.DataFrame(data)

# Boolean Series to filter out certain rows
group_indexes = apps['category'] == 'Utility'

# Applying the boolean index
non_null_readers = apps[group_indexes]['reader'].notnull()

print(non_null_readers)
