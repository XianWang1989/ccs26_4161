
import pandas as pd

# Sample DataFrame
data = {
    'app': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader1', None, 'Reader2']
}
apps = pd.DataFrame(data)

# Boolean Series
group_indexes = pd.Series([False, True, False, True])

# Applying the filter and checking for non-null values in 'reader'
result = apps[group_indexes]['reader'].notnull()

print(result)
