
import pandas as pd
import numpy as np

# Create the sample DataFrame with MultiIndex
index = pd.MultiIndex.from_arrays([
    [1, 1, 1, 1],
    pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01'])
], names=['app', 'regmonth'])

columns = pd.date_range(start='2014-02-01', periods=4, freq='MS')
data = [
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584]
]

df = pd.DataFrame(data, index=index, columns=columns)
print("Original DataFrame:\n", df)

# Transforming the DataFrame
percent_df = df.copy()

# Calculate percentages based on diagonal
for i in range(len(df)):
    diag_value = df.iloc[i, i]
    if diag_value != 0:  # Avoid division by zero
        percent_df.iloc[i] = df.iloc[i] / diag_value

# Display the transformed DataFrame
print("\nTransformed DataFrame:\n", percent_df)
