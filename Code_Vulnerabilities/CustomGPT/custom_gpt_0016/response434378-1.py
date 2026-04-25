
import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'app': ['App1', 'App2', 'App3', 'App4'],
    'reader': [np.nan, 'User1', 'User2', np.nan]
}
apps = pd.DataFrame(data)

# Sample boolean Series (indicating which rows to keep from the DataFrame)
group_indexes = pd.Series([True, False, True, False])

# Boolean indexing and checking for non-null values
result = apps[group_indexes]['reader'].notnull()

print(result)
