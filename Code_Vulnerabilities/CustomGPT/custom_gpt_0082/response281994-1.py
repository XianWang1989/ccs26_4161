
import pandas as pd
import numpy as np

# Sample data creation
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

# Calculating the diagonal values
diagonal_values = df.xs(df.columns[0], level=0, axis=1)

# Transforming the dataframe to percentage relative to diagonal
percentage_df = df.divide(diagonal_values.values, axis=0)

# Including the original values in the desired format
formatted_df = percentage_df.applymap(lambda x: f"{x:.2%}" if np.isfinite(x) else "0.00%")

# Display the result
print(formatted_df)
