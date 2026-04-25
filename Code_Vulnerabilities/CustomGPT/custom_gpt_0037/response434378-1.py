
import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'app_name': ['App1', 'App2', 'App3', 'App4'],
    'reader': [np.nan, 'Reader1', 'Reader2', np.nan]
}
apps = pd.DataFrame(data)

# Define a boolean index Series
group_indexes = apps['reader'].notnull()  # True for non-null 'reader' entries

# Use the boolean index to filter and check for non-null values
result = apps[group_indexes]['reader'].notnull()

print(result)
