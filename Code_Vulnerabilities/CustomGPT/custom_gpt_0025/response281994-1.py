
import pandas as pd

# Sample data creation
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

# Create MultiIndex
index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')],
    names=['app', 'regmonth']
)

# Create DataFrame
df = pd.DataFrame(data, index=index)

# Function to transform the DataFrame
def transform_to_percentage(df):
    diagonal_values = df.xs(df.index[0], level=1)  # Extract diagonal values
    return df.div(diagonal_values.values, axis=0)

# Transform the DataFrame
result_df = transform_to_percentage(df)

print(result_df)
