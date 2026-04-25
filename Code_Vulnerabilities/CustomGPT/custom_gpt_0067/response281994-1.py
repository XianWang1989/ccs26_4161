
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
    (1, '2014-05-01'),
], names=['app', 'regmonth'])

df = pd.DataFrame(data, index=index)

# Function to transform to percentual values
def transform_to_percentage(df):
    # Get the diagonal values
    diagonal = df.xs(df.index[0][0], level=0)

    # Create a new DataFrame with percentual values
    percent_df = df.div(diagonal, axis=0)

    return percent_df

# Transform DataFrame
percent_df = transform_to_percentage(df)

print(percent_df)
