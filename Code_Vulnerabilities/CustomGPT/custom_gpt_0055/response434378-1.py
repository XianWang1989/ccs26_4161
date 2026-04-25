
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [1, None, 3, None]
}

apps = pd.DataFrame(data)

# Sample boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])

# Applying the boolean indexing and checking for non-null values
non_null_readers = apps[group_indexes]['reader'].notnull()

print(non_null_readers)
