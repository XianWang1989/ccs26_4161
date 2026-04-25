
import pandas as pd

# Sample DataFrame
data = {
    'name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader 1', None, 'Reader 2']
}
apps = pd.DataFrame(data)

# Create a boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])  # Only include App1 and App3

# Select 'reader' column for rows indicated by group_indexes and check for non-null values
result = apps[group_indexes]['reader'].notnull()

print(result)
