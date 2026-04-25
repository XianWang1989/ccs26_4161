
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader2', None, 'Reader4'],
}
apps = pd.DataFrame(data)

# Sample boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])

# Use the boolean Series to filter and check for non-null values
result = apps[group_indexes]['reader'].notnull()

print(result)
