
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [5, None, 3, None]
}
apps = pd.DataFrame(data)

# A boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])  # Select App1 and App3

# Filtering the DataFrame based on group_indexes and checking for non-null in 'reader'
filtered_result = apps[group_indexes]['reader'].notnull()

print(filtered_result)
