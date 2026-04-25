
import pandas as pd
import numpy as np

# Sample multiIndex DataFrame setup
arrays = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01'] * 4)
]
index = pd.MultiIndex.from_arrays(arrays, names=['app', 'regmonth'])
data = [
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584]
]
df = pd.DataFrame(data, index=index, columns=pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01']))

# Transforming the DataFrame
for i in range(len(df)):
    diagonal_value = df.iloc[i, i]  # Get diagonal value
    if diagonal_value != 0:  # Prevent division by zero
        df.iloc[i] = df.iloc[i] / diagonal_value

# Display the transformed DataFrame
print(df)
