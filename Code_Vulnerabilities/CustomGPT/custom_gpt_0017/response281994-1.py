
import pandas as pd

# Sample DataFrame creation
index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'),
    (1, '2014-03-01'),
    (1, '2014-04-01'),
    (1, '2014-05-01')
], names=['app', 'regmonth'])

data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

df = pd.DataFrame(data, index=index)

# Transform DataFrame to percentage values
def percentage_from_diagonal(df):
    for i in range(df.shape[0]):
        # Get the diagonal value
        diagonal_value = df.iloc[i, i]
        # Replace counts with percentage
        df.iloc[i] = df.iloc[i] / diagonal_value
    return df

# Apply the transformation
df_percentage = percentage_from_diagonal(df)

# Display the result
print(df_percentage)
