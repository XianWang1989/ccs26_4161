
import pandas as pd

# Sample data
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader2', None, 'Reader4'],
}

apps = pd.DataFrame(data)

# Sample boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])

# Apply the boolean index to filter and check 'reader' column for not null values
not_null_readers = apps[group_indexes]['reader'].notnull()

# Display results
print(not_null_readers)
