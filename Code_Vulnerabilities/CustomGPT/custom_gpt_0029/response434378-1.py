
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader1', None, 'Reader2']
}
apps = pd.DataFrame(data)

# Boolean Series (as an example, let's say we want to filter rows with indices 1 and 3)
group_indexes = pd.Series([False, True, False, True])

# Using the boolean index to filter rows and check for non-null values in the 'reader' column
result = apps[group_indexes]['reader'].notnull()

# Output the result
print(result)
