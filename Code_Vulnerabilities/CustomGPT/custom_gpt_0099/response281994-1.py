
import pandas as pd

# Sample DataFrame with MultiIndex
index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')],
    names=['app', 'regmonth']
)

data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

df = pd.DataFrame(data, index=index)

# Function to calculate percentual values
def transform_to_percentage(df):
    # Extract diagonal values
    diagonal = df.xs(df.index.levels[1][0], level='regmonth', axis=0).values.flatten()

    # Initialize a new DataFrame for the transformed values
    percent_df = df.copy()

    # Calculate percentage based on the diagonal
    for i in range(len(diagonal)):
        row_index = df.index[i][0]  # From multiindex
        percent_df.iloc[i] = df.iloc[i] / diagonal[i] if diagonal[i] != 0 else 0

    return percent_df

# Transform the DataFrame
percent_df = transform_to_percentage(df)

# Display the transformed DataFrame
print(percent_df)
