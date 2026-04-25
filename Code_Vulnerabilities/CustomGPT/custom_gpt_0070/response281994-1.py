
import pandas as pd
import numpy as np

# Sample DataFrame creation
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584],
}
index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')],
    names=['app', 'regmonth']
)

df = pd.DataFrame(data, index=index)

# Calculate the diagonal values
diagonal_values = df.xs(level='regmonth', axis=0, drop_level=False)

# Perform the transformation to percentage values
for i in range(len(diagonal_values)):
    row_index = diagonal_values.index[i]
    divisor = diagonal_values.loc[row_index].values[0]  # Get the diagonal element
    df.loc[row_index] = df.loc[row_index] / divisor  # Divide by the corresponding diagonal value

# Display the transformed DataFrame
print(df)
