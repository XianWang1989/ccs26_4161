
import pandas as pd

# Sample DataFrame
data = {
    'app': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Yes', 'No', None]
}
apps = pd.DataFrame(data)

# Sample boolean Series
group_indexes = pd.Series([True, False, True, False])

# Applying boolean indexing and accessing 'reader' column
result = apps[group_indexes]['reader'].notnull()

print(result)
