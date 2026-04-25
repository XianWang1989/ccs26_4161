
import pandas as pd

# Sample multi-index DataFrame creation
index = pd.MultiIndex.from_tuples(
    [
        (1, '2014-02-01'),
        (1, '2014-03-01'),
        (1, '2014-04-01'),
        (1, '2014-05-01'),
    ],
    names=['app', 'regmonth']
)

columns = pd.MultiIndex.from_tuples(
    [
        ('cnt', '2014-02-01'),
        ('cnt', '2014-03-01'),
        ('cnt', '2014-04-01'),
        ('cnt', '2014-05-01'),
    ],
    names=['loginsmonth', 'date']
)

data = [
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584]
]

df = pd.DataFrame(data, index=index, columns=columns)

# Transform the DataFrame to show percentage of diagonal values
# Get the diagonal values
diagonal_values = df.xs(df.index[0], level='app', axis=0).values.diagonal()

# Iterate through the DataFrame and convert values to percentage of the diagonal
for i, regmonth in enumerate(df.index.levels[1]):
    df.loc[(1, regmonth), :] = df.loc[(1, regmonth), :].div(diagonal_values[i]).round(4)

# Display the transformed DataFrame
print(df)
