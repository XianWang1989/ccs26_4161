
import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}
index = pd.MultiIndex.from_product([[1], pd.date_range('2014-02-01', periods=4, freq='M')])
df = pd.DataFrame(data, index=index)

# Extract diagonal values
diagonal = df.xs(df.columns[0], axis=1, level=0)

# Calculate the percentage values
percent_df = df.div(diagonal, axis=0)

# Display the result
print(percent_df)
