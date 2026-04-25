
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App A', 'App B', 'App C', 'App D'],
    'reader': [None, 'User1', 'User2', None]
}
apps = pd.DataFrame(data)

# Example boolean index Series
group_indexes = pd.Series([True, False, True, False])

# Filtering and checking for non-null values in the 'reader' column
result = apps[group_indexes]['reader'].notnull()

print(result)
