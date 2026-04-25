
import pandas as pd

# Sample data to create the MultiIndex DataFrame
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
    [0, 0, 0, 5584]
]

columns = pd.MultiIndex.from_tuples([
    ('cnt', '2014-02-01'),
    ('cnt', '2014-03-01'),
    ('cnt', '2014-04-01'),
    ('cnt', '2014-05-01'),
])

df = pd.DataFrame(data, index=index, columns=columns)

# Calculate the diagonal values
diagonal_values = df.xs(df.index.get_level_values(0)[0], level='app').values.diagonal()

# Transform to percentage values
for i in range(len(diagonal_values)):
    df.iloc[i] = df.iloc[i] / diagonal_values[i]

# Now df contains the percentage values relative to the diagonal
print(df)
