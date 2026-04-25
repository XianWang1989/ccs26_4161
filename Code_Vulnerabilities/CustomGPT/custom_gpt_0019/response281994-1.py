
import pandas as pd
import numpy as np

# Sample data setup
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'),
     (1, '2014-03-01'),
     (1, '2014-04-01'),
     (1, '2014-05-01')],
    names=['app', 'regmonth']
)

df = pd.DataFrame(data, index=index)

# Extract diagonal values
diagonal_values = df.xs(key='2014-02-01', axis=1, level=1).values.flatten()
index_positions = np.diag_indices(len(diagonal_values))

# Create a mask to apply the diagonal values for the percentual calculation
for i in range(len(diagonal_values)):
    df.iloc[i, :] = df.iloc[i, :] / diagonal_values[i]

# Output the transformed DataFrame
print(df)
