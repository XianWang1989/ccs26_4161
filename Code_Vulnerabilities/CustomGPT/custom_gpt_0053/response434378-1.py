
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader1', None, 'Reader2']
}
apps = pd.DataFrame(data)

# Sample boolean Series (mask)
group_indexes = pd.Series([True, False, True, False])

# Using the boolean index to filter and check for non-null values
result = apps[group_indexes]['reader'].notnull()

print(result)
