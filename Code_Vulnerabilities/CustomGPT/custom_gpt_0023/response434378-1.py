
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader1', None, 'Reader2']
}
apps = pd.DataFrame(data)

# Create a boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])

# Filter the DataFrame and check for non-null values in the 'reader' column
non_null_readers = apps[group_indexes]['reader'].notnull()

# Display the result
print(non_null_readers)
