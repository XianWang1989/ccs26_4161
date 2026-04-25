
import pandas as pd

# Sample data to recreate your multi-index DataFrame
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584],
}

index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01'),
     (2, '2014-02-01'), (2, '2014-03-01'), (2, '2014-04-01'), (2, '2014-05-01'),
     (3, '2014-02-01'), (3, '2014-03-01'), (3, '2014-04-01'), (3, '2014-05-01'),
     (4, '2014-02-01'), (4, '2014-03-01'), (4, '2014-04-01'), (4, '2014-05-01')],
    names=['app', 'regmonth']
)

df = pd.DataFrame(data, index=index)

# Function to transform dataframe to percentage based on diagonal values
def transform_to_percentage(df):
    result = df.copy()
    for i in range(len(df)):
        diag_value = df.iloc[i, i]  # Get the diagonal value
        result.iloc[i] = df.iloc[i] / diag_value if diag_value != 0 else 0  # Avoid division by zero
    return result

# Transform the DataFrame
percent_df = transform_to_percentage(df)

print(percent_df)
