
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'rating': [4.5, None, 4.7, 3.8],
    'reader': [100, None, 150, 200]
}
apps = pd.DataFrame(data)

# Example boolean Series (group_indexes)
group_indexes = pd.Series([True, False, True, True])

# Now we'll filter the DataFrame and check non-null values in the 'reader' column
result = apps[group_indexes]['reader'].notnull()

print(result)
