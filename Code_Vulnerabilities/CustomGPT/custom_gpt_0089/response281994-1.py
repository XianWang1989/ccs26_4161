
import pandas as pd
import numpy as np

# Sample multiIndex DataFrame
arrays = [
    [1, 1, 1, 1]) * 4,
    pd.date_range('2014-02-01', periods=4, freq='MS').tolist() * 4
]
index = pd.MultiIndex.from_product(arrays, names=['app', 'regmonth'])
data = [
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584]
]
df = pd.DataFrame(data, index=index, columns=pd.date_range('2014-02-01', periods=4, freq='MS'))

# Get diagonal values
diagonal_values = df.values.diagonal()

# Create a function to calculate percentage
def calculate_percentages(row, diagonal_value):
    if diagonal_value != 0:
        return row / diagonal_value
    return 0  # Handle division by zero

# Transform the DataFrame
result = df.copy()
for i, (idx, row) in enumerate(df.iterrows()):
    result.loc[idx] = calculate_percentages(row, diagonal_values[i])

print(result)
