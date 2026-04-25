
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': ['Read1', None, 'Read3', None]
}
apps = pd.DataFrame(data)

# Boolean Series for filtering (True for App1 and App3)
group_indexes = pd.Series([True, False, True, False])

# Applying the filtering and checking for non-null values
non_null_readers = apps[group_indexes]['reader'].notnull()

print(non_null_readers)
