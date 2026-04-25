
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': ['Available', None, 'Not available', None]
}
apps = pd.DataFrame(data)

# Boolean Series to filter the DataFrame
group_indexes = pd.Series([True, False, True, True])

# Now applying the filtering and checking for non-null 'reader' values
non_null_readers = apps[group_indexes]['reader'].notnull()

print(non_null_readers)
