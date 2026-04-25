
import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'app': ['App1', 'App2', 'App3', 'App4'],
    'reader': [np.nan, 'Read1', 'Read2', np.nan],
}
apps = pd.DataFrame(data)

# Example boolean Series (say we want to filter based on whether app names start with 'App2' or 'App3')
group_indexes = apps['app'].apply(lambda x: x in ['App2', 'App3'])

# Now we apply the boolean indexing
result = apps[group_indexes]['reader'].notnull()

print("Original DataFrame:")
print(apps)
print("\nBoolean Indexing Result (reader column non-null status):")
print(result)
