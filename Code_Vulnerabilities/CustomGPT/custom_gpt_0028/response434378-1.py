
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader2', 'Reader3', None],
}

apps = pd.DataFrame(data)

# Boolean Series: True for rows we want to keep
group_indexes = pd.Series([False, True, True, False])

# Filtering and checking for not null values in 'reader'
result = apps[group_indexes]['reader'].notnull()

print(result)
