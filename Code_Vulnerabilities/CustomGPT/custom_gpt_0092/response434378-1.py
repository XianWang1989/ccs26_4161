
import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'app_name': ['App A', 'App B', 'App C', 'App D'],
    'reader': [np.nan, 'Reader 1', np.nan, 'Reader 2']
}
apps = pd.DataFrame(data)

# Example boolean Series (True for rows we want to keep)
group_indexes = pd.Series([True, False, True, False])

# Filtering and checking for not null values in 'reader' column
not_null_readers = apps[group_indexes]['reader'].notnull()

print(not_null_readers)
