
import pandas as pd

# Sample DataFrame
data = {
    'reader': [None, 'Alice', 'Bob', None, 'Charlie'],
    'app_name': ['App1', 'App2', 'App3', 'App4', 'App5']
}

apps = pd.DataFrame(data)

# Example group_indexes Series (True for rows to select)
group_indexes = pd.Series([True, False, True, False, True])

# Apply boolean indexing to check for not null in the 'reader' column
result = apps[group_indexes]['reader'].notnull()

print(result)
