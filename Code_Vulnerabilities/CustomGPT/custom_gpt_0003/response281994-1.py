
import pandas as pd
import numpy as np

# Sample data
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'),
    (1, '2014-03-01'),
    (1, '2014-04-01'),
    (1, '2014-05-01')
], names=['app', 'regmonth'])

df = pd.DataFrame(data, index=index)

# Calculate the diagonal elements
diagonal = df.xs(df.index[0], level='regmonth', axis=0)

# Create the percentage DataFrame
percent_df = df.copy()
for i, regmonth in enumerate(percent_df.index.get_level_values('regmonth')):
    if i < len(diagonal):
        percent_df.iloc[i] = percent_df.iloc[i] / diagonal[i]

# Display the transformed DataFrame
print(percent_df)
