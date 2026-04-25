
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

# Calculating percentage values based on the diagonal
def convert_to_percentage(df):
    # Extract diagonal values
    diag = df.xs(df.index[0], level=1)

    # Create a new DataFrame to hold percentage values
    pct_df = df.copy()

    for i in range(len(df)):
        for j in range(len(df.columns)):
            # Reference to the diagonal value
            diag_value = diag.iloc[i][j]
            if diag_value != 0:
                pct_df.iloc[i, j] = f"{df.iloc[i, j]}/{diag_value}"
            else:
                pct_df.iloc[i, j] = '0/0'  # or an appropriate representation for 0

    return pct_df

# Transform the DataFrame
pct_df = convert_to_percentage(df)

# Display the transformed DataFrame
print(pct_df)
