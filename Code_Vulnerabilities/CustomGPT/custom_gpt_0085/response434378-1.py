
import pandas as pd

# Sample DataFrame
data = {
    'name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Text', 'More Text', None]
}
apps = pd.DataFrame(data)

# Sample boolean Series
group_indexes = pd.Series([True, False, True, False])

# Applying the boolean indexing and checking for non-null values in 'reader'
result = apps[group_indexes]['reader'].notnull()

print(result)  # Output will show which 'reader' values are not null for the True rows
