
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App A', 'App B', 'App C', 'App D'],
    'reader': [None, 'Reader B', None, 'Reader D'],
}
apps = pd.DataFrame(data)

# Sample boolean Series for indexing
group_indexes = pd.Series([True, False, True, False])

# Performing the operation
# This will select rows where group_indexes is True and then check for non-null values in the 'reader' column
result = apps[group_indexes]['reader'].notnull()

print(result)
