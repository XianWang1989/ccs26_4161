
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Book Reader', 'Video Reader', None]
}

apps = pd.DataFrame(data)

# Example group_indexes Series
group_indexes = pd.Series([True, False, True, False])

# Filtering using the boolean Series
filtered_reader = apps[group_indexes]['reader'].notnull()

print(filtered_reader)
