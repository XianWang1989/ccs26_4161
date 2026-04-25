
import pandas as pd

# Sample multi-index DataFrame
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
    (1, '2014-05-01'),
], names=['app', 'regmonth'])

df = pd.DataFrame(data, index=index)

# Calculate percentages relative to diagonal
for i in range(len(df)):
    # Get diagonal value for the current row
    diag_value = df.iloc[i, i]
    if diag_value != 0:
        # Divide each value in the row by the diagonal value
        df.iloc[i] = df.iloc[i] / diag_value

print(df)
