
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [5, None, 10, 15]
}
apps = pd.DataFrame(data)

# Sample boolean Series (e.g., filtering apps where reader > 5)
group_indexes = apps['reader'] > 5

# Filtering the 'reader' column using the boolean Series
filtered_readers = apps[group_indexes]['reader']
print(filtered_readers)
