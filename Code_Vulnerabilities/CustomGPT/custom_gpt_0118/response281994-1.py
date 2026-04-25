
import pandas as pd

# Sample data creation
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'),
    (1, '2014-03-01'),
    (1, '2014-04-01'),
    (1, '2014-05-01')
], names=['app', 'regmonth'])

df = pd.DataFrame(data, index=index)
df.columns.names = ['loginsmonth', 'date']

# Calculate percentual values
percent_df = df.copy()
for i in range(len(percent_df)):
    diagonal_value = percent_df.iloc[i, i][0]
    percent_df.iloc[i] = percent_df.iloc[i].div(diagonal_value).fillna(0)

# Display the transformed DataFrame
print(percent_df)
