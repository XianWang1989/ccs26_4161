
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': ['Alice', None, 'Charlie', None]
}
apps = pd.DataFrame(data)

# Boolean Series for filtering (e.g., selecting apps where names start with 'A' or 'C')
group_indexes = apps['app_name'].str.startswith(('A', 'C'))

# Filtering using the boolean Series
result = apps[group_indexes]['reader'].notnull()

print(result)
