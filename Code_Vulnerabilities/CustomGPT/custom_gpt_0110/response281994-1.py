
import pandas as pd

# Sample data creation
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

# Function to calculate the percentage from diagonal
def transform_to_percentage(df):
    # Get the diagonal values
    diagonal = df.xs(df.index[0], level=1, axis=0).values.flatten()

    # Create a new DataFrame to store the percentage values
    percentage_df = df.copy()

    # Apply the transformation
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            if j >= i:  # Only use diagonal values for the calculation
                percentage_df.iat[i, j] = df.iat[i, j] / diagonal[i] if diagonal[i] != 0 else 0

    return percentage_df

# Transform the DataFrame
percentage_df = transform_to_percentage(df)

# Display the transformed DataFrame
print(percentage_df)
