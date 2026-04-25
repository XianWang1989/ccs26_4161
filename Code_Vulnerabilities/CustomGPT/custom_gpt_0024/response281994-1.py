
import pandas as pd

# Sample data
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584],
}
index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')],
    names=['app', 'regmonth']
)
df = pd.DataFrame(data, index=index)

# Calculate the diagonal values
diagonal_values = df.xs(slice(None), level='regmonth').values.diagonal()

# Create a function to divide by the diagonal values
def transform_to_percentage(df):
    result = df.copy()
    for i, diag_value in enumerate(diagonal_values):
        result.iloc[i] = result.iloc[i] / diag_value
    return result

# Apply the transformation
percentage_df = transform_to_percentage(df)

# Display the transformed DataFrame
print(percentage_df)
