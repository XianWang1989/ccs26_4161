
import pandas as pd
import numpy as np

# Sample data creation
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
df.columns = pd.MultiIndex.from_tuples([('cnt', col) for col in df.columns])

# Create a dataframe to hold the transformed values
transformed_df = df.copy()

# Calculate the percentual values
for idx in range(df.shape[0]):
    diagonal_value = df.iloc[idx, idx]  # Get the diagonal value
    if diagonal_value != 0:  # Avoid division by zero
        transformed_df.iloc[idx] = df.iloc[idx] / diagonal_value

# Display the transformed DataFrame
print(transformed_df)
