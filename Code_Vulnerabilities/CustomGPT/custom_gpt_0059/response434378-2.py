
import pandas as pd

# Sample DataFrame
data = {
    'name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Read1', None, 'Read2']
}
apps = pd.DataFrame(data)

# Example boolean Series
group_indexes = pd.Series([True, False, True, False])

# Applying the filtering and notnull method
result = apps[group_indexes]['reader'].notnull()

print(result)
