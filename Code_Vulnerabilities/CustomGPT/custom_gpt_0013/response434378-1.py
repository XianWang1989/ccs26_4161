
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [5, None, 3, None]
}
apps = pd.DataFrame(data)

# Creating a Series of booleans
group_indexes = pd.Series([True, False, True, False])

# Applying the interaction
result = apps[group_indexes]['reader'].notnull()

print(result)
