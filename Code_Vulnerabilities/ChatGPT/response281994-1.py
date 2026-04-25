
import pandas as pd
import numpy as np

# Create the example DataFrame with MultiIndex
arrays = [
    [1, 1, 1, 1],
    pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01'])
]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=['app', 'regmonth'])

data = np.array([
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584]
])

df = pd.DataFrame(data, index=index, columns=pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01']))
df.columns.name = 'loginsmonth'
df = df.sort_index()

# Transform to percentage values based on the diagonal
def transform_to_percentage(df):
    # Get the diagonal elements
    diagonal = df.values[np.arange(df.shape[0]), np.arange(df.shape[0])]

    # Create a new DataFrame for the transformed values
    percentage_df = df.copy()

    # Calculate the percentage values
    for i in range(len(diagonal)):
        if diagonal[i] != 0:
            percentage_df.iloc[i, :] = df.iloc[i, :] / diagonal[i]

    return percentage_df

# Apply the transformation
percentage_df = transform_to_percentage(df)

# Display the transformed DataFrame
print(percentage_df)
