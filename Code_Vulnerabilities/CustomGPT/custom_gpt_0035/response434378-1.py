
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [None, 'Book', 'Magazine', None]
}
apps = pd.DataFrame(data)

# Create a boolean Series for filtering
group_indexes = pd.Series([True, False, True, False])  # True for rows where we want to keep

# Filter based on group_indexes and check which 'reader' values are not null
result = apps[group_indexes]['reader'].notnull()

print(result)
