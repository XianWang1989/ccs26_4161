
import pandas as pd

# Sample data
data = {
    'name': ['App1', 'App2', 'App3', 'App4'],
    'reader': ['Reader1', None, 'Reader3', None]
}
apps = pd.DataFrame(data)

# Boolean Series indicating which rows to include
group_indexes = pd.Series([True, False, True, False])

# Applying the expression
result = apps[group_indexes]['reader'].notnull()

print(result)
