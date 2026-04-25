
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader2', None, 'Reader4']
}
apps = pd.DataFrame(data)

# Sample boolean index
group_indexes = pd.Series([True, False, True, False])

# Apply boolean indexing and check for non-null values in the 'reader' column
result = apps[group_indexes]['reader'].notnull()

print(result)
