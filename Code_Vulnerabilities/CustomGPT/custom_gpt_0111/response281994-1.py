
import pandas as pd
import numpy as np

# Creating the sample multi-index DataFrame
arrays = [
    [1, 1, 1, 1],
    pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01']),
]
index = pd.MultiIndex.from_arrays(arrays, names=('app', 'regmonth'))

data = [
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584],
]
df = pd.DataFrame(data, index=index, columns=pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01']))
df.columns.name = 'loginsmonth'

# Transforming to percentage of diagonal
percent_df = df.copy()

for (app, regmonth), row in df.iterrows():
    diagonal_value = row[regmonth].values[0]
    if diagonal_value != 0:
        percent_df.loc[(app, regmonth)] = row / diagonal_value

# Display the transformed DataFrame
print(percent_df)
