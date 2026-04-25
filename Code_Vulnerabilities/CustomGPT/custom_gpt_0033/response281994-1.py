
import pandas as pd
import numpy as np

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

# Calculate percentual values related to the diagonal
for idx in range(len(df)):
    diagonal_value = df.iloc[idx, idx]  # Value on the diagonal
    if diagonal_value != 0:  # Prevent division by zero
        df.iloc[idx] = df.iloc[idx] / diagonal_value

# Format DataFrame to decimal percentage
df = df.applymap(lambda x: f"{x:.2f}" if isinstance(x, (float, np.float64)) else x)

# Display the transformed DataFrame
print(df)
