
import pandas as pd

# Sample DataFrame
data = {
    'name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [1, None, 3, None]
}
apps = pd.DataFrame(data)

# Boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])

# Using the boolean Series to filter and check for non-null in 'reader' column
result = apps[group_indexes]['reader'].notnull()

print(result)
