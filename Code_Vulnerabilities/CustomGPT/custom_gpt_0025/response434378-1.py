
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App A', 'App B', 'App C', 'App D'],
    'reader': [None, 'Reader 1', 'Reader 2', None]
}
apps = pd.DataFrame(data)

# Creating a boolean Series, for example, filtering apps that are not None
group_indexes = apps['reader'].notnull()

# Accessing the 'reader' column for the filtered rows
result = apps[group_indexes]['reader'].notnull()

# Display the result
print(result)
