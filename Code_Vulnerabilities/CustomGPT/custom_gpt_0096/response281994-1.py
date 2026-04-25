
import pandas as pd

# Sample MultiIndex DataFrame
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')],
    names=['app', 'regmonth']
)

df = pd.DataFrame(data, index=index)

# Extract diagonal values
diagonal_values = df.xs(key='2014-02-01', level='regmonth', axis=0).values

# Transform DataFrame to percentual values
df_transformed = df.div(diagonal_values, axis=0)

print(df_transformed)
