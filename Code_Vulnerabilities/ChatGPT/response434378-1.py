
import pandas as pd

# Sample DataFrame
data = {
    'app': ['AppA', 'AppB', 'AppC', 'AppD'],
    'reader': [None, 'Reader1', None, 'Reader2'],
}

apps = pd.DataFrame(data)

# Let's say we want to filter based on some condition
# For example, we might want to select apps based on some criteria
group_indexes = pd.Series([True, False, True, False])  # Boolean index

# Now we filter the DataFrame
filtered_readers = apps[group_indexes]['reader'].notnull()

print(filtered_readers)
