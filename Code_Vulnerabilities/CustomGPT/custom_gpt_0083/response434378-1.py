
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader 2', 'Reader 3', None]
}
apps = pd.DataFrame(data)

# Creating a boolean Series
group_indexes = pd.Series([True, False, True, False])

# Filtering and checking for non-null values in the 'reader' column
results = apps[group_indexes]['reader'].notnull()

print(results)
