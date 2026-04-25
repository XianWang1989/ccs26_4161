
import pandas as pd
import numpy as np

# Sample MultiIndex DataFrame
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584],
}

index = pd.MultiIndex.from_arrays(
    [
        [1, 1, 1, 1],
        pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01'])
    ],
    names=['app', 'regmonth']
)

df = pd.DataFrame(data, index=index)

# Transform DataFrame to percentual values based on the diagonal
def transform_to_percent(df):
    for idx in range(len(df)):
        diagonal_value = df.iloc[idx, idx]  # Get diagonal value
        if diagonal_value != 0:
            df.iloc[idx] = df.iloc[idx] / diagonal_value  # Divide row by diagonal value
    return df

# Apply transformation
percent_df = transform_to_percent(df.copy())

print(percent_df)
