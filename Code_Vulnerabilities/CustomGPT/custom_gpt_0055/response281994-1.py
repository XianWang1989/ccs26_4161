
import pandas as pd

# Sample DataFrame creation with MultiIndex
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_tuples([(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')], names=['app', 'regmonth'])
df = pd.DataFrame(data, index=index)

# Calculate percentual values related to diagonal
percent_df = df.copy()
for idx in df.index:
    regmonth = idx[1]
    diagonal_value = df.xs(regmonth, level='regmonth', axis=0).iloc[0, 0]
    percent_df.loc[idx] = df.loc[idx] / diagonal_value

# Displaying the transformed DataFrame
print(percent_df)
