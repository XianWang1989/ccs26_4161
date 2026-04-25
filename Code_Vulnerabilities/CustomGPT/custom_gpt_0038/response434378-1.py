
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader2', None, 'Reader4']
}
apps = pd.DataFrame(data)

# Boolean Series to filter the DataFrame
group_indexes = pd.Series([True, False, True, False])

# Applying the filtering and checking for non-null values
result = apps[group_indexes]['reader'].notnull()

print(result)
