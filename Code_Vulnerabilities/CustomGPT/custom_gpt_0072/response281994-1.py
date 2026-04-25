
import pandas as pd
import numpy as np

# Sample multi-index DataFrame creation
arrays = [
    [1, 1, 1, 1],
    pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01'])
]
index = pd.MultiIndex.from_arrays(arrays, names=['app', 'regmonth'])
data = [
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584]
]
df = pd.DataFrame(data, index=index, columns=pd.date_range('2014-02-01', periods=4, freq='M'))
df.columns.name = 'loginsmonth'

# Transforming to percentual values related to the diagonal
percent_df = df.copy()
for i in range(len(df)):
    row_index = df.index[i][1]  # Get the 'regmonth' part
    diagonal_value = df.loc[(1, row_index), row_index]  # Get the diagonal value
    if diagonal_value != 0:  # Avoid division by zero
        percent_df.iloc[i] = df.iloc[i] / diagonal_value

# Displaying the transformed DataFrame
print(percent_df)
