
import pandas as pd

# Sample DataFrame
data = {
    'name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader2', None, 'Reader4']
}
apps = pd.DataFrame(data)

# Sample boolean Series for indexing
group_indexes = pd.Series([True, False, True, False])

# Filtering and checking for non-null values
result = apps[group_indexes]['reader'].notnull()
print(result)
