
import pandas as pd

# Sample data
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584],
}
index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')
], names=['app', 'regmonth'])
df = pd.DataFrame(data, index=index)

# Function to calculate percentages
def calculate_percentages(df):
    # Get the diagonal values
    diagonal_values = df.xs(df.index[0][0], level='app', axis=0).values.flatten()
    result = df.copy()

    for col_idx, col in enumerate(df.columns):
        result.iloc[:, col_idx] = df.iloc[:, col_idx] / diagonal_values[col_idx]
        result.iloc[:, col_idx] = result.iloc[:, col_idx].apply(lambda x: f"{x:.4f}/{diagonal_values[col_idx]}")

    return result

# Applying the function
transformed_df = calculate_percentages(df)

# Display the transformed DataFrame
print(transformed_df)
