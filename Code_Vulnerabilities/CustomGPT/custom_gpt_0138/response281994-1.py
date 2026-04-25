
import pandas as pd

# Sample DataFrame creation
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_arrays(
    [[1, 1, 1, 1], ['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01']],
    names=['app', 'regmonth']
)

df = pd.DataFrame(data, index=index)

# Transform to percentage based on diagonal
def transform_to_percentage(df):
    for i in range(len(df)):
        diag_value = df.iloc[i, i][0]  # Get the diagonal value
        df.iloc[i] = df.iloc[i] / diag_value  # Divide the entire row by diagonal value
    return df

percentage_df = transform_to_percentage(df)
print(percentage_df)
