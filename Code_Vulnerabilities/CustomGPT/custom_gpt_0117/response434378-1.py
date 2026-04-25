
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Read1', None, 'Read2']
}
apps = pd.DataFrame(data)

# Sample boolean Series
group_indexes = pd.Series([True, False, True, False])

# Applying the operation
result = apps[group_indexes]['reader'].notnull()

print(result)
