
import pandas as pd

# Create a sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader2', 'Reader3', None]
}
apps = pd.DataFrame(data)

# Create a boolean Series for the rows we want to filter
group_indexes = pd.Series([True, False, True, False])

# Filter the DataFrame using the boolean Series and check the 'reader' column for null values
result = apps[group_indexes]['reader'].notnull()

print(result)
