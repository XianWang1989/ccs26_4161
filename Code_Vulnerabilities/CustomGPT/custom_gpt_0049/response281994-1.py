
import pandas as pd

# Sample DataFrame creation
arrays = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ['2014-02-01', '2014-02-01', '2014-03-01', '2014-03-01', '2014-04-01', '2014-04-01', '2014-05-01', '2014-05-01', '2014-05-01', '2014-05-01', '2014-05-01', '2014-05-01']
]
index = pd.MultiIndex.from_arrays(arrays, names=['app', 'regmonth'])
data = [
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584]
]
df = pd.DataFrame(data, index=index, columns=pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01']))
df.index = df.index.set_names(['app', 'regmonth'])

# Function to transform the DataFrame
def normalize_to_diagonal(df):
    # Convert DataFrame to a float type for calculation
    df = df.astype(float)
    # Get each diagonal element
    diagonal = df.values.diagonal()

    # Calculate percentages
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            if diagonal[i] != 0:  # Avoid division by zero
                df.iat[i, j] = df.iat[i, j] / diagonal[i]

    return df

# Transform the DataFrame
percent_df = normalize_to_diagonal(df)

# Display the transformed DataFrame
print(percent_df)
