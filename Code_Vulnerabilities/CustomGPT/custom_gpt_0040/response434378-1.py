
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader1', None, 'Reader2'],
}
apps = pd.DataFrame(data)

# Sample boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])

# Filtering and checking for non-null values in 'reader'
result = apps[group_indexes]['reader'].notnull()

print(result)
