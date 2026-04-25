
import pandas as pd

# Create the multiIndex DataFrame
arrays = [
    [1, 1, 1, 1],
    pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01'])
]
index = pd.MultiIndex.from_arrays(arrays, names=['app', 'regmonth'])

data = {
    pd.to_datetime('2014-02-01'): [6069, 0, 0, 0],
    pd.to_datetime('2014-03-01'): [1837, 10742, 0, 0],
    pd.to_datetime('2014-04-01'): [107, 2709, 5584, 0],
    pd.to_datetime('2014-05-01'): [54, 1387, 1103, 5584]
}

df = pd.DataFrame(data, index=index)
df = df.rename(columns=lambda x: 'cnt')

# Calculate percentage based on diagonal
for i in range(len(df)):
    val = df[cnt].iloc[i, i]
    df.iloc[i] = df.iloc[i] / val if val != 0 else 0

print(df)
