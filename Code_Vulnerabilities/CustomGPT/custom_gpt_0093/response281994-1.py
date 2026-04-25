
import pandas as pd
import numpy as np

# Create the multi-index DataFrame
index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')],
    names=['app', 'regmonth']
)

data = np.array([
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584]
])

columns = pd.date_range(start='2014-02-01', periods=4, freq='MS')
df = pd.DataFrame(data, index=index, columns=columns)

# Calculate the diagonal values
diagonal = df.values[np.arange(df.shape[0]), np.arange(df.shape[1])]

# Create a new DataFrame with percentage values
percent_df = df.div(diagonal, axis=0)

# Display the resulting DataFrame
print(percent_df)
