
import pandas as pd
import numpy as np

# Sample data creation
index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'),
    (1, '2014-03-01'),
    (1, '2014-04-01'),
    (1, '2014-05-01')
], names=['app', 'regmonth'])

data = np.array([
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584]
])

# Creating the multi-index DataFrame
df = pd.DataFrame(data, index=index, columns=pd.date_range(start='2014-02-01', periods=4, freq='MS'))
print("Original DataFrame:")
print(df)

# Transforming to percentual values related to the diagonal
for i in range(len(df)):
    diagonal_value = df.iloc[i, i]  # Get the diagonal value
    if diagonal_value != 0:  # Avoid division by zero
        df.iloc[i] = df.iloc[i] / diagonal_value

print("\nTransformed DataFrame:")
print(df)
