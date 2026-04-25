
import pandas as pd
import numpy as np

# Sample multi-index DataFrame
index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'), 
     (1, '2014-03-01'), 
     (1, '2014-04-01'), 
     (1, '2014-05-01')],
    names=['app', 'regmonth']
)

columns = pd.MultiIndex.from_product(
    [['cnt'], ['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01']],
    names=['loginsmonth', 'date']
)

data = np.array([
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584]
])

df = pd.DataFrame(data, index=index, columns=columns)

# Calculate diagonal values for each row
diagonal_values = df.xs('cnt', axis=1, level=0).values.diagonal()

# Transform the DataFrame to percentage values
result_df = df.xs('cnt', axis=1, level=0).copy()

for i in range(len(diagonal_values)):
    result_df.iloc[i] = result_df.iloc[i] / diagonal_values[i]

# To show result in percentage format
result_df = result_df.applymap(lambda x: '{:.2%}'.format(x))

# Output the resulting DataFrame
result_df.columns = pd.MultiIndex.from_product([['cnt'], result_df.columns], names=['loginsmonth', 'date'])
print(result_df)
