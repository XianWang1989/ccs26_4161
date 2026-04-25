
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader1', None, 'Reader2']
}
apps = pd.DataFrame(data)

# Boolean Series for filtering
group_indexes = apps['reader'].notnull()  # True for non-null reader values

# Using the boolean Series to filter
not_null_readers = apps[group_indexes]['reader'].notnull()

print(not_null_readers)
