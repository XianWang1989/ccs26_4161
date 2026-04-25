
import pandas as pd

# Sample MultiIndex DataFrame
index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')],
    names=['app', 'regmonth']
)
data = {
    '2014-02-01': [6069, 0, 0, 0],
    '2014-03-01': [1837, 10742, 0, 0],
    '2014-04-01': [107, 2709, 5584, 0],
    '2014-05-01': [54, 1387, 1103, 5584]
}
df = pd.DataFrame(data, index=index)

# Transforming the DataFrame
for col in df.columns:
    diag_value = df.xs(col, level='regmonth').iloc[0]
    df[col] = df[col] / diag_value * 100

# Display the transformed DataFrame
print(df)
