
import pandas as pd
import numpy as np

# Sample multi-index DataFrame creation
arrays = [
    [1, 1, 1, 1],
    pd.date_range('2014-02-01', periods=4, freq='M')
]
index = pd.MultiIndex.from_arrays(arrays, names=('app', 'regmonth'))

data = np.array([
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584]
])

df = pd.DataFrame(data, index=index, columns=pd.date_range('2014-02-01', periods=4, freq='M'))
print("Original DataFrame:")
print(df)

# Transforming to percentage based on the diagonal
for i in range(len(df)):
    diagonal_value = df.iloc[i, i]  # Get the diagonal value
    if diagonal_value != 0:  # Avoid division by zero
        df.iloc[i] = df.iloc[i] / diagonal_value

print("\nTransformed DataFrame with Percentage Values:")
print(df)
