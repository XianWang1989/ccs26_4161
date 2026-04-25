
import pandas as pd

# Create the multi-index DataFrame
index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01'),
    (2, '2014-02-01'), (2, '2014-03-01'), (2, '2014-04-01'), (2, '2014-05-01')
], names=['app', 'regmonth'])

data = [
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584]
]

df = pd.DataFrame(data, columns=pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01']), index=index)
df.columns = pd.MultiIndex.from_product([['cnt'], df.columns])

# Transform the values into percentages against the diagonal
for i in range(len(df)):
    # Get the diagonal value
    diagonal_value = df.iloc[i, i, 0]
    if diagonal_value != 0:
        df.iloc[i] = df.iloc[i] / diagonal_value

# Display the transformed DataFrame
print(df)
