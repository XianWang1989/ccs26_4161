
import pandas as pd

# Sample data
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader1', None, 'Reader2']
}
apps = pd.DataFrame(data)

# Example boolean Series
group_indexes = pd.Series([True, False, True, False])

# Filtering the DataFrame
result = apps[group_indexes]['reader'].notnull()

# Display the result
print(result)
