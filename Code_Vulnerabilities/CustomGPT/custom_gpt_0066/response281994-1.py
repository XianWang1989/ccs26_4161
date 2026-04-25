
import pandas as pd

# Sample data
data = {
    ('loginsmonth', '2014-02-01'): [6069, 0, 0, 0],
    ('loginsmonth', '2014-03-01'): [1837, 10742, 0, 0],
    ('loginsmonth', '2014-04-01'): [107, 2709, 5584, 0],
    ('loginsmonth', '2014-05-01'): [54, 1387, 1103, 5584],
}
index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')
], names=['app', 'regmonth'])

df = pd.DataFrame(data, index=index)

# Transform to percentage values related to the diagonal
for i in df.index:
    diagonal_value = df.loc[i, (slice(None), i[1])]
    df.loc[i] = df.loc[i] / diagonal_value.values

# Display the transformed DataFrame
print(df)
