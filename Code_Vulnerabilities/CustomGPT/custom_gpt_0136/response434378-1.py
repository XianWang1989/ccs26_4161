
import pandas as pd

# Sample DataFrame
data = {
    'name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader2', 'Reader3', None]
}
apps = pd.DataFrame(data)

# Boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])

# Using boolean indexing with the 'reader' column
result = apps[group_indexes]['reader'].notnull()

print(result)
