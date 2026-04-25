
import pandas as pd

# Sample multi-index DataFrame creation
arrays = [
    [1, 1, 1, 1],  # app
    pd.date_range('2014-02-01', periods=4, freq='M')  # regmonth
]
index = pd.MultiIndex.from_arrays(arrays, names=['app', 'regmonth'])
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}
df = pd.DataFrame(data, index=index)

# Transforming the DataFrame to percentage values using the diagonal
result = df.copy()

for i in range(len(result)):
    diagonal_value = df['cnt'].iloc[i, i]  # Diagonal element
    result.iloc[i] = df.iloc[i] / diagonal_value

# Display the result
print(result)
