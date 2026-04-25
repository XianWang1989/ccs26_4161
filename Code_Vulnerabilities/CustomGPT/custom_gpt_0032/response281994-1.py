
import pandas as pd
import numpy as np

# Sample data creation
index = pd.MultiIndex.from_tuples([(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')])
columns = pd.MultiIndex.from_product([['cnt'], ['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01']])
data = [[6069, 1837, 107, 54],
        [0, 10742, 2709, 1387],
        [0, 0, 5584, 1103],
        [0, 0, 0, 5584]]

df = pd.DataFrame(data, index=index, columns=columns)

# Function to transform values to percentages related to diagonal
def transform_to_percent(df):
    diagonal = np.diagonal(df.values)  # Get the diagonal elements
    for i in range(len(diagonal)):
        df.iloc[i, :] = df.iloc[i, :] / diagonal[i]  # Divide each row by the diagonal element
    return df

# Apply the transformation
transformed_df = transform_to_percent(df)

# Display the transformed DataFrame
print(transformed_df)
