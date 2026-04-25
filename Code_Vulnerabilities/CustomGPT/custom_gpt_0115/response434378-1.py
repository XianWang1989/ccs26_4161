
import pandas as pd

# Sample DataFrame
data = {
    'name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'This is a reader', 'Another reader', None]
}
apps = pd.DataFrame(data)

# Boolean Series
group_indexes = pd.Series([True, False, True, False])

# Applying the boolean mask and accessing the 'reader' column
result = apps[group_indexes]['reader'].notnull()

print(result)
