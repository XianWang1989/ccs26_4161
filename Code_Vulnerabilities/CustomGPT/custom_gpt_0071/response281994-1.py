
import pandas as pd

# Create a sample DataFrame
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

# Function to transform DataFrame to percentage based on diagonal
def percentage_transform(df):
    # Extract diagonal values
    diagonal = df.xs(df.index[0][1]).values

    # Calculate the percentage
    for i, idx in enumerate(df.index):
        df.loc[idx] = df.loc[idx] / diagonal[i]

    return df

# Transform the DataFrame
transformed_df = percentage_transform(df)
print(transformed_df)
