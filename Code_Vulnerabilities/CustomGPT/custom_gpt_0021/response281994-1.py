
import pandas as pd
import numpy as np

# Sample multi-index DataFrame
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}
index = pd.MultiIndex.from_tuples([(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')],
                                   names=['app', 'regmonth'])
df = pd.DataFrame(data, index=index)

# Get diagonal values
diagonal_values = np.diag(df.values)

# Create a percentage DataFrame
percent_df = df.copy()
for i in range(len(diagonal_values)):
    percent_df.iloc[i] = df.iloc[i] / diagonal_values[i]  # Percentage calculation

# Display the result
print(percent_df)
