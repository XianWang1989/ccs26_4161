
import pandas as pd
import numpy as np

# Sample MultiIndex DataFrame
index = pd.MultiIndex.from_tuples([(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')], 
                                   names=['app', 'regmonth'])
data = np.array([[6069, 1837, 107, 54],
                 [0, 10742, 2709, 1387],
                 [0, 0, 5584, 1103],
                 [0, 0, 0, 5584]])

df = pd.DataFrame(data, index=index, columns=pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01']))
df = df.stack().rename("cnt").reset_index()
df = df.set_index(['app', 'regmonth'])

# Transforming to percentage relative to diagonal
for i in range(len(df)):
    app, regmonth = df.index[i]
    diagonal_value = df.loc[(app, regmonth), 'cnt']
    df.loc[(app, regmonth), 'cnt'] = df.loc[(app, regmonth), 'cnt'] / diagonal_value if diagonal_value != 0 else 0

# Reshaping back to original MultiIndex structure
df = df.unstack(level='regmonth')
# Example of formatting the dataframe to display as percentages
df = df.apply(lambda x: (x.astype(float) / df.xs(df.columns[0], level=1, axis=1)).fillna(0), axis=1)

print(df)
