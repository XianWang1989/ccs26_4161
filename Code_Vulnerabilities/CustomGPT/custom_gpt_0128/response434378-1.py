
import pandas as pd

# Sample DataFrame
data = {
    'name': ['App1', 'App2', 'App3', 'App4'],
    'reader': ['User1', None, 'User3', None]
}
apps = pd.DataFrame(data)

# Example boolean Series (True for rows we want to include)
group_indexes = pd.Series([True, False, True, False])

# Filtering the DataFrame and checking 'reader' column for not null values
result = apps[group_indexes]['reader'].notnull()

print(result)
