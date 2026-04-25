
import pandas as pd
import numpy as np

# Sample DataFrame creation
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

# Function to calculate percentage
def transform_to_percentage(df):
    # Get diagonal values
    diagonal_values = df.xs(df.index[0][1], level=1, axis=0).values.flatten()

    # Apply the transformation
    percent_df = df.copy()
    for i, idx in enumerate(df.index):
        percent_df.loc[idx] = df.loc[idx] / diagonal_values[i]

    return percent_df

# Transform the DataFrame
percent_df = transform_to_percentage(df)

# Display the result
print(percent_df)
