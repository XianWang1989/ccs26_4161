
import pandas as pd

# Sample DataFrame
data = {
    'name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'BookReader', 'VideoReader', None]
}
apps = pd.DataFrame(data)

# Create a boolean Series
group_indexes = apps['reader'].notnull()  # True where 'reader' is not None

# Applying the boolean Series to filter the DataFrame
filtered_readers = apps[group_indexes]['reader']

print(filtered_readers)
