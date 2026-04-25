
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'PDF', None, 'EPUB']
}
apps = pd.DataFrame(data)

# Example boolean Series
group_indexes = pd.Series([True, False, True, False])

# Using boolean indexing and checking for not null
result = apps[group_indexes]['reader'].notnull()

# Displaying the result
print(result)
