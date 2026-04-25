
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'ReaderA', None, 'ReaderB']
}
apps = pd.DataFrame(data)

# Sample boolean Series
group_indexes = pd.Series([True, False, True, False])

# Using the boolean index to filter and check for non-null values
result = apps[group_indexes]['reader'].notnull()

# Outputting the result
print(result)
