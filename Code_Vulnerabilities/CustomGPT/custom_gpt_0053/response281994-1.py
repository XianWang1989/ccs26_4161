
import pandas as pd

# Sample data creation
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_tuples([(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')])
df = pd.DataFrame(data, index=index)

# Convert the DataFrame's multi-index to columns for easier processing
df.columns = df.columns.droplevel(0)

# Calculate percentages relative to the diagonal
for i in range(len(df)):
    diag_value = df.iloc[i, i]  # Get the diagonal value
    df.iloc[i] = df.iloc[i] / diag_value if diag_value else 0  # Avoid division by zero

# Display the transformed DataFrame
print(df)
