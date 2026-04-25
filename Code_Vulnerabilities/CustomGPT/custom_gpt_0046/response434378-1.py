
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Yes', None, 'No']
}
apps = pd.DataFrame(data)

# Example boolean Series (mask)
group_indexes = pd.Series([True, False, True, False])

# Applying the interaction
result = apps[group_indexes]['reader'].notnull()

print(result)
