
import pandas as pd

# Sample multiIndex DataFrame
arrays = [
    ['1', '1', '1', '1'],
    ['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01']
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

# Transforming the DataFrame
for i in range(len(df)):
    denominator = df.iloc[i, i]
    if denominator != 0:
        df.iloc[i] = df.iloc[i] / denominator

print(df)
