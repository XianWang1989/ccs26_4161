
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': ['Yes', None, 'No', 'Yes']
}
apps = pd.DataFrame(data)

# Boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])

# Interacting with the DataFrame
filtered_readers = apps[group_indexes]['reader'].notnull()

print(filtered_readers)
