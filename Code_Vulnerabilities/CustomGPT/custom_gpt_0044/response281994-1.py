
import pandas as pd

# Sample multi-index DataFrame
index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'),
    (1, '2014-03-01'),
    (1, '2014-04-01'),
    (1, '2014-05-01'),
], names=['app', 'regmonth'])

data = [
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584],
]

df = pd.DataFrame(data, index=index, columns=pd.date_range('2014-02-01', periods=4, freq='MS'))
df.columns.name = 'loginsmonth'

# Transforming to percentages relative to the diagonal
for col in range(df.shape[1]):
    diagonal_value = df.iloc[col, col]
    if diagonal_value != 0:  # Avoid division by zero
        df.iloc[col] = df.iloc[col] / diagonal_value

# Display the transformed DataFrame
print(df)
