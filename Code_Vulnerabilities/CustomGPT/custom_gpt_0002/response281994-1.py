
import pandas as pd

# Sample multiIndex DataFrame
arrays = [
    [1, 1, 1, 1],
    pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01'])
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

# Transform to percentual values
for row in range(len(df)):
    for col in range(len(df.columns)):
        diagonal_value = df.iloc[row, row]  # Get the diagonal value
        if diagonal_value != 0:  # Avoid division by zero
            df.iat[row, col] = df.iat[row, col] / diagonal_value

print(df)
