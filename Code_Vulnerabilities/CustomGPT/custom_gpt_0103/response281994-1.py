
import pandas as pd
import numpy as np

# Sample data creation
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584],
}
index = pd.MultiIndex.from_tuples([(1, '2014-02-01'), 
                                    (1, '2014-03-01'), 
                                    (1, '2014-04-01'), 
                                    (1, '2014-05-01')], 
                                    names=['app', 'regmonth'])

df = pd.DataFrame(data, index=index)

# Calculate the diagonal elements
diagonal_values = np.diagonal(df.values)

# Function to calculate percentage
def percent_from_diagonal(df):
    for i in range(len(diagonal_values)):
        df.iloc[i] = df.iloc[i] / diagonal_values[i]
    return df

# Apply the function
percentage_df = percent_from_diagonal(df)

# Display the transformed DataFrame
print(percentage_df)
