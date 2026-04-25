
import pandas as pd
import numpy as np

# Sample MultiIndex DataFrame
index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'),
    (1, '2014-03-01'),
    (1, '2014-04-01'),
    (1, '2014-05-01')
], names=['app', 'regmonth'])

data = {
    '2014-02-01': [6069, 0, 0, 0],
    '2014-03-01': [1837, 10742, 0, 0],
    '2014-04-01': [107, 2709, 5584, 0],
    '2014-05-01': [54, 1387, 1103, 5584]
}

df = pd.DataFrame(data, index=index)
df.columns.name = 'loginsmonth'
df = df.stack().reset_index(name='cnt')
df = df.set_index(['app', 'regmonth'])

# Transforming to percentage relative to the diagonal
for i in range(len(df.index.levels[1])):
    diag_value = df.xs(df.index.levels[1][i], level='regmonth').iloc[i]['cnt']
    df.xs(df.index.levels[1][i], level='regmonth')['cnt'] = df.xs(df.index.levels[1][i], level='regmonth')['cnt'] / diag_value

# Reshape back to the original form
df = df.unstack().fillna(0)

print(df)
