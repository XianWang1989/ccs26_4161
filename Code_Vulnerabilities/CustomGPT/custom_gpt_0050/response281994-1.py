
import pandas as pd

# Sample multi-index DataFrame
arrays = [
    [1, 1, 1, 1],
    ['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01']
]
index = pd.MultiIndex.from_arrays(arrays, names=['app', 'regmonth'])

data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}
df = pd.DataFrame(data, index=index)

# Calculate the diagonal values
diagonal_values = df.xs('2014-02-01')['cnt'].values
diagonal_values = df['cnt'].iloc[::4].values  # Extract diagonal values

# Transform the DataFrame
df_percent = df.copy()
for i, date in enumerate(df.columns.levels[1]):
    df_percent.iloc[:, i] = df.iloc[:, i] / diagonal_values[i]

# Display the transformed DataFrame
df_percent
