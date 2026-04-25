
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

# Calculate the percentage relative to the diagonal
for idx in df.index:
    diagonal_value = df.loc[idx, ('cnt', idx[1])]  # Getting the diagonal value
    if diagonal_value != 0:  # Avoiding division by zero
        df.loc[idx] = df.loc[idx] / diagonal_value

# Print the transformed DataFrame
print(df)
