
import pandas as pd
import numpy as np

# Sample DataFrame creation
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

# Transforming the DataFrame to percentage
# Extract diagonal elements
diagonal = df.xs('2014-02-01', level='regmonth', axis=0)

# Vectorized operation to compute percentage
df_percent = df.div(diagonal.values, axis=0)

# Display result
print(df_percent)
