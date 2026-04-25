
import pandas as pd

# Sample data
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')],
    names=['app', 'regmonth']
)

df = pd.DataFrame(data, index=index)

# Calculate the diagonal values
diagonal = df.xs(df.columns[0], level=1, axis=1).values.flatten()

# Apply the transformation
percent_df = df.copy()

for i in range(len(diagonal)):
    percent_df.iloc[i] = df.iloc[i] / diagonal[i] * 100

# Print the transformed DataFrame
print(percent_df)
