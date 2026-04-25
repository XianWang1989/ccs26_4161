
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader2', 'Reader3', None]
}
apps = pd.DataFrame(data)

# Example boolean Series for indexing
group_indexes = apps['reader'].notnull()  # This will create a boolean Series

# Applying boolean indexing and checking for not null in the 'reader' column
result = apps[group_indexes]['reader'].notnull()

print(result)
