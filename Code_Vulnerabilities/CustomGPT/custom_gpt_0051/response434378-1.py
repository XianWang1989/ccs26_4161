
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader2', 'Reader3', None]
}
apps = pd.DataFrame(data)

# Boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])

# Interaction: Filter the DataFrame and check not null
result = apps[group_indexes]['reader'].notnull()

print(result)
