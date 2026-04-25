
import pandas as pd

# Create a sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': ['User1', None, 'User3', 'User4']
}
apps = pd.DataFrame(data)

# Create a boolean Series for filtering
group_indexes = pd.Series([True, False, True, True])

# Filter the DataFrame and check for non-null 'reader' values
non_null_readers = apps[group_indexes]['reader'].notnull()

print(non_null_readers)
