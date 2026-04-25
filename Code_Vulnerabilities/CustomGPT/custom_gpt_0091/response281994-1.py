
import pandas as pd

# Sample multi-index DataFrame
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}
index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')],
    names=['app', 'regmonth']
)
df = pd.DataFrame(data, index=index)

# Function to compute percentage relative to the diagonal values
def transform_to_percentage(df):
    # Get the diagonal values
    diag_values = df.xs(df.index[0][0], level=0).values.flatten()

    # Create a new DataFrame for the percentage transformation
    percent_df = df.copy()

    for i, col in enumerate(df.columns):
        percent_df[col] = df[col] / diag_values[i]

    return percent_df

# Applying the transformation
percent_df = transform_to_percentage(df)

print(percent_df)
