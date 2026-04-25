
import pandas as pd
import numpy as np

# Create the sample DataFrame with MultiIndex
arrays = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01',
                    '2014-03-01', '2014-04-01', '2014-05-01', '2014-05-01'])
]
index = pd.MultiIndex.from_arrays(arrays, names=('app', 'regmonth'))
data = [
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584]
]
df = pd.DataFrame(data, index=index, columns=pd.date_range('2014-02-01', periods=4, freq='MS'))
print("Original DataFrame:")
print(df)

# Function to calculate percentual values
def to_percentual_values(df):
    # Extract diagonal elements
    diagonal_values = np.diag(df.values)

    # Calculate percentual values relative to diagonal
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            if diagonal_values[i] != 0:  # avoid division by zero
                df.iat[i, j] = df.iat[i, j] / diagonal_values[i]

    return df

# Transform the DataFrame
percentual_df = to_percentual_values(df.copy())
print("\nTransformed DataFrame:")
print(percentual_df)
