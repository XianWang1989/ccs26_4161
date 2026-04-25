
import pandas as pd

# Example DataFrame
data = {
    'app_name': ['App A', 'App B', 'App C', 'App D'],
    'reader': [None, 'Reader 1', 'Reader 2', None]
}
apps = pd.DataFrame(data)

# Boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])

# Filtering and checking for non-null values in 'reader' column
result = apps[group_indexes]['reader'].notnull()

print(result)
