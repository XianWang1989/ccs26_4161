
import pandas as pd
import numpy as np

# Sample multiIndex DataFrame
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584],
}

index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')],
    names=['app', 'regmonth']
)

df = pd.DataFrame(data, index=index)

# Transforming to percentage values
for col in df.columns.levels[1]:
    diagonal_value = df.xs(col, level=1, axis=1).iloc[0, 0]
    df.xs(col, level=1, axis=1) /= diagonal_value

# Display the transformed DataFrame
print(df)
