
import pandas as pd
import numpy as np

# Sample data creation
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
df.columns = pd.MultiIndex.from_tuples(df.columns)

# Function to transform values
def transform_to_percentages(df):
    # Get diagonal values
    diagonal = np.diagonal(df.values, offset=0)

    # Create a new DataFrame to hold the percentage values
    percentage_df = df.copy()

    # Loop through the DataFrame and perform the transformation
    for i in range(len(diagonal)):
        for j in range(len(percentage_df.columns)):
            if df.values[i, i] != 0:  # Avoid division by zero
                percentage_df.iloc[i, j] = df.iloc[i, j] / df.values[i, i]
            else:
                percentage_df.iloc[i, j] = 0  # Handle zero cases appropriately

    return percentage_df

# Transform DataFrame
percentage_df = transform_to_percentages(df)
print(percentage_df)
