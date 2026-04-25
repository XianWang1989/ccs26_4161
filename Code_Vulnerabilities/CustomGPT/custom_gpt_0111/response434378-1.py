
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader1', None, 'Reader2']
}
apps = pd.DataFrame(data)

# Boolean Series indicating which rows to filter (e.g., select rows where app_name starts with 'App1' or 'App2')
group_indexes = apps['app_name'].isin(['App1', 'App2'])

# Using the boolean indexer to filter and check 'reader' column for non-null values
result = apps[group_indexes]['reader'].notnull()

# Display the result
print(result)
