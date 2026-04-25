
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader1', 'Reader2', None]
}
apps = pd.DataFrame(data)

# Boolean Series to filter the DataFrame (selecting rows where app_name is 'App2' or 'App4')
group_indexes = apps['app_name'].isin(['App2', 'App4'])

# Now using the boolean Series to filter 'reader' column for not null values
result = apps[group_indexes]['reader'].notnull()

print(result)
