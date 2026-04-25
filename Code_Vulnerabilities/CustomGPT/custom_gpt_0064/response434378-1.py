
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'User1', None, 'User2']
}
apps = pd.DataFrame(data)

# Boolean Series to filter rows
group_indexes = pd.Series([True, False, True, False])

# Using the boolean Series to filter and check for not null
result = apps[group_indexes]['reader'].notnull()

print(result)
