
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'User1', 'User2', None]
}
apps = pd.DataFrame(data)

# Example boolean Series
group_indexes = pd.Series([True, False, True, False])  # Selecting rows 0 and 2

# Accessing the 'reader' column with boolean indexing
result = apps[group_indexes]['reader'].notnull()

print(result)
