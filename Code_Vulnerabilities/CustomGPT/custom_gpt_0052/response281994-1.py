
import pandas as pd

# Sample multi-index DataFrame
arrays = [
    ['1', '1', '1', '1'],
    ['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01'],
]
index = pd.MultiIndex.from_arrays(arrays, names=('app', 'regmonth'))
data = [
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584]
]
df = pd.DataFrame(data, index=index, columns=pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01']))

# Function to convert to percentage of diagonal elements
def transform_to_percentage(df):
    # Get the diagonal values
    diagonal_values = df.values.diagonal()

    # Create a new DataFrame to hold the transformed values
    percentage_df = df.copy()

    # Iterate through the DataFrame and transform the values
    for i in range(len(diagonal_values)):
        percentage_df.iloc[i] = df.iloc[i] / diagonal_values[i]

    return percentage_df

# Transforming the DataFrame
transformed_df = transform_to_percentage(df)

# Display the transformed DataFrame
print(transformed_df)
