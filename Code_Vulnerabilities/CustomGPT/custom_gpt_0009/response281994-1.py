
import pandas as pd
import numpy as np

# Sample data creation
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_tuples([(1, '2014-02-01'), (1, '2014-03-01'), 
                                    (1, '2014-04-01'), (1, '2014-05-01')])
df = pd.DataFrame(data, index=index)

# Transforming the DataFrame
for i in range(len(df.index)):
    diagonal_value = df.iloc[i, i]  # Get the diagonal value
    if diagonal_value != 0:  # Avoid division by zero
        df.iloc[i] = df.iloc[i] / diagonal_value

df = df.round(4)  # Optional: Round the values for better readability
print(df)
