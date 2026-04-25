
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App A', 'App B', 'App C', 'App D'],
    'reader': [5, None, 8, None]
}
apps = pd.DataFrame(data)

# Assume group_indexes is a boolean Series
group_indexes = pd.Series([True, False, True, False])

# Applying the boolean index to filter and check for non-null values
result = apps[group_indexes]['reader'].notnull()

print(result)
