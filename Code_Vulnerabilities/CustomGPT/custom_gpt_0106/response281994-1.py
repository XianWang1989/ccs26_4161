
import pandas as pd
import numpy as np

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

# Transforming the DataFrame
def transform_dataframe(df):
    diagonal = df.xs(df.index[0][1], level=1)  # Get diagonal values
    for col in df.columns:
        df[col] = df[col] / diagonal[col]
    return df

# Applying the transformation
transformed_df = transform_dataframe(df)

# Displaying the transformed DataFrame
print(transformed_df)
