
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App A', 'App B', 'App C', 'App D'],
    'reader': ['Yes', None, 'No', 'Yes']
}
apps = pd.DataFrame(data)

# Boolean Series to filter rows
group_indexes = pd.Series([True, False, True, True])

# Applying the filtering and accessing the 'reader' column
result = apps[group_indexes]['reader'].notnull()

# Display result
print(result)
