
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [1, None, 3, 4]
}
apps = pd.DataFrame(data)

# Sample boolean Series (same length as the DataFrame)
group_indexes = pd.Series([True, False, True, False])

# Filtering the DataFrame and checking for non-null values in the 'reader' column
non_null_readers = apps[group_indexes]['reader'].notnull()

print(non_null_readers)
