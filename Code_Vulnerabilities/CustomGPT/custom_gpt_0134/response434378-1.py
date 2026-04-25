
import pandas as pd

# Sample DataFrame
data = {
    'name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader2', None, 'Reader4'],
    'category': ['Game', 'Social', 'Utility', 'Game']
}

apps = pd.DataFrame(data)

# Boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])

# Applying the boolean Series to filter and check for non-null in 'reader' column
non_null_readers = apps[group_indexes]['reader'].notnull()

# Display the result
print(non_null_readers)
