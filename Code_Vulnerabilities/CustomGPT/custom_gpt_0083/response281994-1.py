
import pandas as pd

# Sample data creation
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

# Create MultiIndex
index = pd.MultiIndex.from_tuples([(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')], names=['app', 'regmonth'])
df = pd.DataFrame(data, index=index)

# Calculate diagonal values
diagonal = df.xs(df.index[0], level='app').values.diagonal()

# Transform to percentage
for i in range(len(diagonal)):
    df.iloc[i] = df.iloc[i] / diagonal[i]

# Optional: Format the output
df = df.applymap(lambda x: f"{x:.2%}" if x > 0 else "0")

print(df)
