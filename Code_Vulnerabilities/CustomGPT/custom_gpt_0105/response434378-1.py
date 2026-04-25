
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [1, None, 3, None],
}
apps = pd.DataFrame(data)

# Sample boolean Series
group_indexes = pd.Series([True, False, True, False])

# Filter the DataFrame
filtered_readers = apps[group_indexes]['reader'].notnull()

print(filtered_readers)
