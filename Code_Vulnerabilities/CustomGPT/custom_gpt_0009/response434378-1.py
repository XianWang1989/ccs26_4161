
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': ['Text', None, 'Audio', 'Video']
}
apps = pd.DataFrame(data)

# Boolean Series for group indexes
group_indexes = pd.Series([True, False, True, False])

# Apply boolean indexing and check for non-null values in the 'reader' column
non_null_readers = apps[group_indexes]['reader'].notnull()

# Output the result
print(non_null_readers)
