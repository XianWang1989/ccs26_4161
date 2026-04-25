
import pandas as pd

# Create a sample DataFrame
data = {
    'app_name': ['App A', 'App B', 'App C', 'App D'],
    'reader': [None, 'Reader B', None, 'Reader D']
}
apps = pd.DataFrame(data)

# Create a boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])

# Filter the DataFrame and check for non-null values in the 'reader' column
result = apps[group_indexes]['reader'].notnull()

print(result)
