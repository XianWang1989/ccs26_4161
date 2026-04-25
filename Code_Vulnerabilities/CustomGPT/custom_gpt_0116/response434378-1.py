
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App A', 'App B', 'App C', 'App D'],
    'reader': [None, 'User 1', None, 'User 2']
}
apps = pd.DataFrame(data)

# Boolean Series representing some condition (e.g., presence of 'User 1')
group_indexes = pd.Series([False, True, False, True], index=apps.index)

# Applying boolean indexing and checking for non-null values
result = apps[group_indexes]['reader'].notnull()

print(result)
