
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App A', 'App B', 'App C', 'App D'],
    'reader': [None, 'Reader B', None, 'Reader D']
}

apps = pd.DataFrame(data)

# Assume we create a boolean mask that selects certain rows
group_indexes = pd.Series([True, False, True, False])  # This mask selects 'App A' and 'App C'

# Now we are using that mask to filter apps and check for non-null 'reader'
non_null_readers = apps[group_indexes]['reader'].notnull()

print(non_null_readers)
