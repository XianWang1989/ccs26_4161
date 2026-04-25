
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader2', 'Reader3', None]
}
apps = pd.DataFrame(data)

# Boolean Series for filtering rows
group_indexes = pd.Series([True, False, True, False])  # Selecting App1 and App3

# Applying the boolean indexing and checking for not-null values
result = apps[group_indexes]['reader'].notnull()

print(result)
