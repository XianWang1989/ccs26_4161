
import pandas as pd

# Sample data
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
    (1, '2014-05-01'),
], names=['app', 'regmonth'])

# Create the DataFrame
df = pd.DataFrame(data, index=index)

# Function to transform DataFrame values to percentage of diagonal
def transform_to_percentage(df):
    # Get diagonal values
    diagonal = df.xs(df.index[0], level='regmonth')
    # Create a percentage DataFrame
    percent_df = df.divide(diagonal.values, axis=1)
    # Format the values as fractions
    for col in percent_df.columns:
        percent_df[col] = percent_df[col].apply(lambda x: f"{x}/{diagonal[col].values[0]}")
    return percent_df

# Applying the transformation
result_df = transform_to_percentage(df)
print(result_df)
