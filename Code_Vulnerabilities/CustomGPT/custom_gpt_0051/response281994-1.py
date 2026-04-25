
import pandas as pd

# Sample DataFrame creation
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584],
}
index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'),
    (1, '2014-03-01'),
    (1, '2014-04-01'),
    (1, '2014-05-01')
], names=['app', 'regmonth'])

df = pd.DataFrame(data, index=index)

# Transforming the DataFrame
for i in range(4):  # Assuming the DataFrame is a 4x4
    diag_value = df.iloc[i, i]  # Get the diagonal value
    df.iloc[i] = df.iloc[i] / diag_value if diag_value != 0 else 0  # Calculate percentage

# Display the transformed DataFrame
print(df)
