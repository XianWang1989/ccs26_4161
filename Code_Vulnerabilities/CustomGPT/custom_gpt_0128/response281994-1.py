
import pandas as pd

# Sample DataFrame creation
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584],
}
index = pd.MultiIndex.from_tuples([(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')])
df = pd.DataFrame(data, index=index)

# Transforming to percentual values related to the diagonal
diagonal = df.xs(key='2014-02-01', level=1, axis=0)  # Get diagonal values for each column
for col in df.columns:
    df.loc[(1, slice(None)), col] = df.loc[(1, slice(None)), col] / diagonal[col]

# Display the transformed DataFrame
print(df)
