
import pandas as pd
import numpy as np

# Sample data
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_tuples([(1, '2014-02-01'), (1, '2014-03-01'),
                                    (1, '2014-04-01'), (1, '2014-05-01')],
                                   names=['app', 'regmonth'])

df = pd.DataFrame(data, index=index)

# Function to transform the DataFrame
def transform_to_percentage(df):
    # Get diagonal values
    diagonal_values = df.xs(df.index[0][1], level=1, axis=0)

    # Create a new DataFrame to hold percentage values
    percentage_df = df.copy()

    for col in df.columns:
        # Get the diagonal value for the current column
        diag_value = diagonal_values[col]
        # Divide each element by the diagonal value
        percentage_df[col] = df[col] / diag_value

    return percentage_df

# Transform the DataFrame
result_df = transform_to_percentage(df)

# Display the result
print(result_df)
