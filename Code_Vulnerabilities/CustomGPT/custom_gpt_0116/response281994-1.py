
import pandas as pd

# Sample data
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_product([[1], pd.date_range(start='2014-02-01', periods=4)], names=['app', 'regmonth'])
df = pd.DataFrame(data, index=index)

# Transforming to percentage of the diagonal
for i in range(len(df.index)):
    diagonal_value = df.iloc[i, i]  # get the diagonal value
    df.iloc[i] = df.iloc[i] / diagonal_value  # divide the row by the diagonal value

# Print the transformed DataFrame
print(df)
