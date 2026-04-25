
import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'app_name': ['App A', 'App B', 'App C', 'App D'],
    'reader': [None, 'Reader B', 'Reader C', None]
}
apps = pd.DataFrame(data)

# Boolean Series, where True corresponds to App A and App C
group_indexes = pd.Series([True, False, True, False])

# Using the boolean Series to filter the DataFrame and check for non-null 'reader' values
non_null_readers = apps[group_indexes]['reader'].notnull()

print(non_null_readers)
