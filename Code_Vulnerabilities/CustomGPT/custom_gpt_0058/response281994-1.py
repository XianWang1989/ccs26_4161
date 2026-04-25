
import pandas as pd

# Create the initial multiIndex DataFrame
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}
index = pd.MultiIndex.from_tuples([(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')])
df = pd.DataFrame(data, index=index)

# Set the column names to have multiIndex style
df.columns = pd.MultiIndex.from_product([['cnt'], df.columns.levels[1]])

# Calculate diagonal values
diagonal = df.xs('cnt', axis=1, level=0).values.diagonal()

# Transform to percentage
percent_df = df.copy()
for i in range(len(diagonal)):
    percent_df.iloc[i] = df.iloc[i] / diagonal[i]

print(percent_df)
