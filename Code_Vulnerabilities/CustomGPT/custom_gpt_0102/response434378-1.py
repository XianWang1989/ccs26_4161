
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader2', None, 'Reader4']
}
apps = pd.DataFrame(data)

# Creating a boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])

# Using the boolean Series to filter and then check for non-null values in 'reader' column
not_null_readers = apps[group_indexes]['reader'].notnull()

print(not_null_readers)
