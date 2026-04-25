
import pandas as pd

# Sample data creation
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

# Calculate percentual values relative to the diagonal
def transform_percentile(df):
    for i in range(len(df)):
        diagonal_value = df.iloc[i, i]  # Element along the diagonal
        df.iloc[i] = df.iloc[i] / diagonal_value  # Update the row's values
    return df

# Transform the DataFrame
percent_df = transform_percentile(df)

# Display the transformed DataFrame
print(percent_df)
