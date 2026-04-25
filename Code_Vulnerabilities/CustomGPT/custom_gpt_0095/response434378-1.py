
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [10, None, 5, None],
    'category': ['Game', 'Utility', 'Game', 'Tool']
}

apps = pd.DataFrame(data)

# Create a boolean Series for filtering
group_indexes = apps['reader'].notnull()  # This will be True for rows where 'reader' is not None

# Using the boolean Series to filter
filtered_readers = apps[group_indexes]['reader']

print(filtered_readers)
