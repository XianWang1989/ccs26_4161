
import pandas as pd

# Sample DataFrame setup
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
    (1, '2014-05-01'),
], names=['app', 'regmonth'])

df = pd.DataFrame(data, index=index)

# Transform to percentual values relative to diagonal
def transform_percent(df):
    for col, row in df.iterrows():
        # Get the diagonal value
        diagonal_value = df.at[(row.name[0], row.name[1]), col]
        # Calculate percentual values
        df.at[row.name, col] = row[col] / diagonal_value if diagonal_value != 0 else 0
    return df

# Apply transformation
df_transformed = transform_percent(df)

print(df_transformed)
