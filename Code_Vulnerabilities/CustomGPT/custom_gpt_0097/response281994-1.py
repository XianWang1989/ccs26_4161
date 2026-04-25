
import pandas as pd

# Sample multi-index DataFrame
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584],
}
index = pd.MultiIndex.from_tuples([(1, '2014-02-01'), 
                                    (1, '2014-03-01'), 
                                    (1, '2014-04-01'), 
                                    (1, '2014-05-01')])
df = pd.DataFrame(data, index=index)

# Transform to percentual values
for i in range(len(df)):
    diagonal_value = df.iloc[i, i][0]  # Get the diagonal value
    df.iloc[i, :] = df.iloc[i, :] / diagonal_value  # Divide by diagonal value

# Print the transformed DataFrame
print(df)
