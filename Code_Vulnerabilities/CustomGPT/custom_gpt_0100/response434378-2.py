
import pandas as pd

# Sample DataFrame
data = {
    'app': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader2', 'Reader3', None],
}
apps = pd.DataFrame(data)

# Sample Boolean Series
group_indexes = pd.Series([False, True, True, False])

# Applying the boolean index to filter 'reader' column
result = apps[group_indexes]['reader'].notnull()

print(result)
