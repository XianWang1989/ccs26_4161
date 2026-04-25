
import pandas as pd
import numpy as np

# Sample multi-index DataFrame creation
index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01'),
], names=['app', 'regmonth'])

columns = pd.date_range(start='2014-02-01', periods=4, freq='MS')
data = np.array([
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584]
])

df = pd.DataFrame(data, index=index, columns=columns)

# Transforming to percentage based on the diagonal values
def percentage_transform(df):
    result = df.copy()
    for idx in df.index.levels[0]:  # Loop through app indices
        diag_value = df.loc[idx, idx].values[0]  # Get the diagonal value
        result.loc[idx] = df.loc[idx] / diag_value  # Apply percentage transformation
    return result

# Apply the transformation
percentage_df = percentage_transform(df)

# Display the resulting DataFrame
print(percentage_df)
