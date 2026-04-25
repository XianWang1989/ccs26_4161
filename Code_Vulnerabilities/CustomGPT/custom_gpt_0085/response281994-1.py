
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
    [(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')],
    names=['app', 'regmonth']
)

df = pd.DataFrame(data, index=index)

# Transforming the DataFrame
percent_df = df.copy()

for i in range(len(df.index)):
    row_index = df.index[i][1]  # Get the regmonth for diagonal reference
    diag_value = df.xs(row_index, level='regmonth').iloc[i, 0]  # Get diagonal value
    percent_df.iloc[i] = df.iloc[i] / diag_value  # Calculate percentages

# Display the transformed DataFrame
percent_df = percent_df.fillna(0)  # Fill NaN with 0 for better readability
print(percent_df)
