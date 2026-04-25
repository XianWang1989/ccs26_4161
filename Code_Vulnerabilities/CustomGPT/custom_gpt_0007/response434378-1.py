
import pandas as pd

# Sample data
data = {
    'app_name': ['App A', 'App B', 'App C', 'App D'],
    'reader': [None, 'Reader B', 'Reader C', None]
}
apps = pd.DataFrame(data)

# Assume this is our boolean indexing Series
group_indexes = pd.Series([True, False, True, False])

# Using the boolean index to filter the DataFrame and check for non-null values in 'reader'
result = apps[group_indexes]['reader'].notnull()

# Display the result
print(result)
