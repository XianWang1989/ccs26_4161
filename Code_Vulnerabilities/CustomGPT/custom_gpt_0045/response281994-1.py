
import pandas as pd

# Sample multiIndex DataFrame
arrays = [
    [1, 1, 1, 1],
    pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01'])
]
index = pd.MultiIndex.from_arrays(arrays, names=('app', 'regmonth'))

data = {
    pd.to_datetime('2014-02-01'): [6069, 0, 0, 0],
    pd.to_datetime('2014-03-01'): [1837, 10742, 0, 0],
    pd.to_datetime('2014-04-01'): [107, 2709, 5584, 0],
    pd.to_datetime('2014-05-01'): [54, 1387, 1103, 5584],
}
df = pd.DataFrame(data, index=index)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Transforming to percentage values relative to diagonal
def transform_to_percentage(df):
    # Create an empty DataFrame for the results
    result = df.copy()

    for i in range(len(df)):
        # Get the diagonal element for the current row's index
        diagonal_value = df.iloc[i, i]

        # Apply transformation
        if diagonal_value != 0:  # Avoid division by zero
            result.iloc[i] = df.iloc[i] / diagonal_value
        else:
            result.iloc[i] = 0  # Handle division by zero case

    return result

# Apply the transformation
percentage_df = transform_to_percentage(df)

# Display the transformed DataFrame
print("\nTransformed DataFrame (Percentages):")
print(percentage_df)
