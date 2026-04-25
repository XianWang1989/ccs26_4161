
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'ReaderA', None, 'ReaderB']
}
apps = pd.DataFrame(data)

# Boolean Series to select specific rows (e.g., where app_name starts with 'App')
group_indexes = apps['app_name'].str.startswith('App')

# Using the boolean index to filter and then check for non-null values in 'reader'
non_null_readers = apps[group_indexes]['reader'].notnull()

print(non_null_readers)
