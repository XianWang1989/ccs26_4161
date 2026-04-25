
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Reader2', None, 'Reader4'],
}
apps = pd.DataFrame(data)

# Boolean Series (for example, filtering out apps that contain '1' or '3')
group_indexes = apps['app_name'].str.contains('1|3')

# Now using the boolean indexing with the 'reader' column
result = apps[group_indexes]['reader'].notnull()

print(result)
