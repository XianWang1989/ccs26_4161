
import pandas as pd

# Create a sample DataFrame
data = {
    'app_name': ['App A', 'App B', 'App C', 'App D'],
    'reader': [None, 'Reader1', 'Reader2', None]
}
apps = pd.DataFrame(data)

# Let's say we have a boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])

# Now we apply the indexing and check for non-null values
result = apps[group_indexes]['reader'].notnull()

print(result)
