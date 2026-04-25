
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App A', 'App B', 'App C', 'App D'],
    'reader': [None, 'Reader 1', 'Reader 2', None]
}
apps = pd.DataFrame(data)

# Sample boolean Series
group_indexes = pd.Series([True, False, True, False])

# Using boolean indexing with notnull
result = apps[group_indexes]['reader'].notnull()

print(result)
