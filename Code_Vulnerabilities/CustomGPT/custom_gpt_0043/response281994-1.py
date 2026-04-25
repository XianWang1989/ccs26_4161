
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
    [(1, '2014-02-01'), (1, '2014-03-01'),
     (1, '2014-04-01'), (1, '2014-05-01')],
    names=['app', 'regmonth']
)

df = pd.DataFrame(data, index=index)

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Calculate percent values based on the diagonal
def transform_to_percentage(df):
    # Get the diagonal values
    diagonal_values = np.diagonal(df.to_numpy())
    # Create a new DataFrame to store the percentages
    percentage_df = df.copy() 

    for i, regmonth in enumerate(df.index.levels[1]): 
        # Get the appropriate diagonal value
        diagonal_value = diagonal_values[i]
        # Calculate the percentages
        percentage_df[i] = df[i] / diagonal_value if diagonal_value != 0 else 0

    return percentage_df

# Transform the DataFrame
result_df = transform_to_percentage(df)

# Display resulting DataFrame
print("\nTransformed DataFrame (Percentages):")
print(result_df)
