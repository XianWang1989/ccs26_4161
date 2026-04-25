
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'reader2', 'reader3', None],
    'rating': [4.5, 3.5, 5.0, 2.0]
}
apps = pd.DataFrame(data)

# Sample boolean Series (group_indexes)
group_indexes = pd.Series([True, False, True, False])

# Executing the expression
result = apps[group_indexes]['reader'].notnull()

# Display the result
print(result)
