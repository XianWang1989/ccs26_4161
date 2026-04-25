
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Read', 'Read', None]
}
apps = pd.DataFrame(data)

# Example boolean Series
group_indexes = pd.Series([False, True, True, False])

# Interacting with the DataFrame
result = apps[group_indexes]['reader'].notnull()

print(result)
