
import pandas as pd

# Sample DataFrame
data = {
    'name': ['App A', 'App B', 'App C', 'App D'],
    'reader': [None, 'Reader 1', None, 'Reader 2']
}
apps = pd.DataFrame(data)

# Example boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])

# Filtering and checking for non-null values
result = apps[group_indexes]['reader'].notnull()

print(result)
