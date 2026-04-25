
import pandas as pd
import numpy as np

# Sample data
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

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Function to transform to percentage of diagonal
def transform_to_percentage(df):
    diagonal = np.diagonal(df.values)  # Get diagonal values
    percentages = df.values / diagonal[:, np.newaxis]  # Calculate percentages
    transformed_df = pd.DataFrame(percentages, columns=df.columns, index=df.index)  # Create new DataFrame
    return transformed_df

# Transforming the DataFrame
transformed_df = transform_to_percentage(df)

# Formatting output for percentage representation
transformed_df = transformed_df.applymap(lambda x: f"{x:.2%}")

# Display the transformed DataFrame
print("\nTransformed DataFrame (Percentages):")
print(transformed_df)
