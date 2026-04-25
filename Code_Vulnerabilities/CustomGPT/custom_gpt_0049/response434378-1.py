
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader1', 'Reader2', None]
}
apps = pd.DataFrame(data)

# Simulating group_indexes as a boolean Series
group_indexes = pd.Series([True, False, True, False])

# Using the expression
result = apps[group_indexes]['reader'].notnull()

print(result)
