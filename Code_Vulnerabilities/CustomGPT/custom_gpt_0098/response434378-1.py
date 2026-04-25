
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'UserA', None, 'UserB']
}
apps = pd.DataFrame(data)

# Sample boolean Series for filtering
group_indexes = pd.Series([True, False, True, True])

# Applying the filter and notnull
result = apps[group_indexes]['reader'].notnull()

print(result)
