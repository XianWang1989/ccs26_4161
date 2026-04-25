
import pandas as pd

# Sample DataFrame with MultiIndex
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

# Create MultiIndex
index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'),
    (1, '2014-03-01'),
    (1, '2014-04-01'),
    (1, '2014-05-01'),
], names=['app', 'regmonth'])

# Create the DataFrame
df = pd.DataFrame(data, index=index)

# Function to calculate percentage based on diagonal values
def transform_to_percentage(df):
    new_df = df.copy()
    for i in range(len(df)):
        diagonal_value = df.iloc[i][i]  # Get the diagonal element
        if diagonal_value != 0:  # Avoid division by zero
            new_df.iloc[i] = df.iloc[i] / diagonal_value
    return new_df

# Apply the transformation
transformed_df = transform_to_percentage(df)

# Display the transformed DataFrame
print(transformed_df)
