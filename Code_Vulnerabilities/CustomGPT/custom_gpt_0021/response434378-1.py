
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App A', 'App B', 'App C', 'App D'],
    'reader': [None, 'Reader 1', None, 'Reader 2']
}
apps = pd.DataFrame(data)

# Sample Boolean index (e.g., apps where the app_name is 'App A' or 'App C')
group_indexes = pd.Series([True, False, True, False])

# Using the boolean index to filter rows and then checking for not null in 'reader'
result = apps[group_indexes]['reader'].notnull()

print(result)
