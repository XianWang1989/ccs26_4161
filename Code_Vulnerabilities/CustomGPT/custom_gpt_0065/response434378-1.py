
import pandas as pd

# Sample DataFrame
data = {
    'name': ['app1', 'app2', 'app3', 'app4'],
    'reader': [None, 'Reader2', 'Reader3', None],
}
apps = pd.DataFrame(data)

# Boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])

# Filtering and checking for non-null values in the 'reader' column
non_null_readers = apps[group_indexes]['reader'].notnull()

print(non_null_readers)
