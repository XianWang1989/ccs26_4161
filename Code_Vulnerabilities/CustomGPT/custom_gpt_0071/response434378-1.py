
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader1', 'Reader2', None]
}
apps = pd.DataFrame(data)

# Sample Boolean Series
group_indexes = pd.Series([True, False, True, False])

# Applying the filtering
non_null_readers = apps[group_indexes]['reader'].notnull()

print(non_null_readers)
