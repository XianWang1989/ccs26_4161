
import pandas as pd

# Sample multi-index DataFrame
index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')],
    names=['app', 'regmonth']
)
columns = pd.MultiIndex.from_tuples(
    [( 'cnt', '2014-02-01'), ( 'cnt', '2014-03-01'), ( 'cnt', '2014-04-01'), ( 'cnt', '2014-05-01')],
)
data = [
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584],
]

df = pd.DataFrame(data, index=index, columns=columns)

# Transforming to percentual values related to the diagonal
for i in range(len(df)):
    diagonal_value = df.iloc[i, i]
    df.iloc[i] = df.iloc[i] / diagonal_value if diagonal_value != 0 else 0

print(df)
