
import pandas as pd

# Sample DataFrame construction
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

# Calculating the percentual values
percent_df = df.copy()
for i in range(len(df)):
    diagonal_value = df['cnt'].iloc[i, i]
    percent_df['cnt'].iloc[i] = df['cnt'].iloc[i] / diagonal_value if diagonal_value else 0

# Displaying the transformed DataFrame
print(percent_df)
