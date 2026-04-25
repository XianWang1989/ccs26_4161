
import pandas as pd
import numpy as np

# Sample data creation
index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'),
    (1, '2014-03-01'),
    (1, '2014-04-01'),
    (1, '2014-05-01'),
],
    names=['app regmonth', 'loginsmonth'])

data = np.array([
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584]
])

df = pd.DataFrame(data, index=index, columns=pd.date_range('2014-02-01', periods=4, freq='M'))
print("Original DataFrame:")
print(df)

# Function to transform the DataFrame
def transform_to_percentage(df):
    # Access the diagonal values
    diagonal = df.values.diagonal()

    # Perform the division and replace the values in the DataFrame
    for i, idx in enumerate(df.index.levels[0]):
        if diagonal[i] != 0:  # Avoid division by zero
            df.xs(idx).iloc[:, :] = df.xs(idx) / diagonal[i]
    return df

# Transform DataFrame to percentage
transformed_df = transform_to_percentage(df)
print("\nTransformed DataFrame with Percentages:")
print(transformed_df)
