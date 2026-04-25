
import pandas as pd

# Sample multiindex DataFrame
arrays = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    ['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01'] * 4
]
index = pd.MultiIndex.from_arrays(arrays, names=['app', 'regmonth'])
data = [
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584]
]
df = pd.DataFrame(data, index=index, columns=pd.date_range('2014-02-01', periods=4, freq='MS'))

# Normalize values by the diagonal
for i in range(len(df)):
    diagonal_value = df.iloc[i, i]  # Get diagonal element
    if diagonal_value != 0:  # Avoid division by zero
        df.iloc[i] = df.iloc[i] / diagonal_value

print(df)
