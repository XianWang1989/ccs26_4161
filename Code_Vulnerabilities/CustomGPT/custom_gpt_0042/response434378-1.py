
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader1', None, 'Reader2']
}
apps = pd.DataFrame(data)

# Sample boolean indexing Series
group_indexes = pd.Series([True, False, True, False])

# Filtering the DataFrame based on group_indexes and checking for non-null values in 'reader'
result = apps[group_indexes]['reader'].notnull()

# Display the results
print(result)
