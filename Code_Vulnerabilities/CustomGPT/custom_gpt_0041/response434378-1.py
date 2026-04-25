
import pandas as pd

# Sample DataFrame
data = {
    'name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [1, None, 3, None]
}
apps = pd.DataFrame(data)

# Boolean Series
group_indexes = pd.Series([True, False, True, False])

# Applying the boolean index and checking for non-null values
result = apps[group_indexes]['reader'].notnull()

print(result)
