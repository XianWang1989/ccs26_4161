
import pandas as pd
import numpy as np

# Sample MultiIndex DataFrame
index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')
], names=['app', 'regmonth'])

data = [[6069, 1837, 107, 54],
        [0, 10742, 2709, 1387],
        [0, 0, 5584, 1103],
        [0, 0, 0, 5584]]

df = pd.DataFrame(data, columns=pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01']),
                  index=index)

# Convert to MultiIndex DataFrame with a 'cnt' level
df = df.stack().reset_index(name='cnt')
df = df.set_index(['app', 'regmonth']).unstack(fill_value=0)

# Calculate percentage based on the diagonal
for i in range(df.shape[0]):
    diagonal_value = df.iloc[i, i]
    df.iloc[i, :] = df.iloc[i, :] / diagonal_value

# Clean up DataFrame and display results
df.columns = df.columns.droplevel(0)  # Remove the top-level 'cnt'
print(df)
