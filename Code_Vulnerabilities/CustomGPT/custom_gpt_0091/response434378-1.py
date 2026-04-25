
import pandas as pd

# Sample DataFrame
data = {
    'name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader2', None, 'Reader4']
}
apps = pd.DataFrame(data)

# Sample boolean Series (for example, filtering even-indexed rows)
group_indexes = pd.Series([True, False, True, False])

# Select 'reader' where group_indexes is True and check for non-null values
result = apps[group_indexes]['reader'].notnull()

print(result)
