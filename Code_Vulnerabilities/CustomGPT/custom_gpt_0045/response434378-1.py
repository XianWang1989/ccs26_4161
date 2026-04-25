
import pandas as pd

# Sample data
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader2', 'Reader3', None]
}

# Create DataFrame
apps = pd.DataFrame(data)

# Define a boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])  # Filter apps where index is 0 or 2

# Filter the DataFrame and check for non-null values in the 'reader' column
not_null_readers = apps[group_indexes]['reader'].notnull()

print(not_null_readers)
