
import pandas as pd
import numpy as np

# Sample DataFrame initialization
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}
index = pd.MultiIndex.from_tuples([(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')],
                                   names=['app', 'regmonth'])
df = pd.DataFrame(data, index=index)

# Function to transform into percentage of diagonal values
def transform_to_percentage(df):
    # Get the diagonal values
    diagonal_values = np.diag(df.xs('cnt', axis=1, level=0).values)

    # Create a new DataFrame for the percentage values
    percentage_df = df.copy()

    for i in range(len(diagonal_values)):
        # Divide each row by the corresponding diagonal value
        percentage_df.iloc[i] = df.iloc[i] / diagonal_values[i] * 100 if diagonal_values[i] != 0 else 0

    return percentage_df

# Transform the DataFrame
percentage_df = transform_to_percentage(df)

# Print the resulting DataFrame
print(percentage_df)
