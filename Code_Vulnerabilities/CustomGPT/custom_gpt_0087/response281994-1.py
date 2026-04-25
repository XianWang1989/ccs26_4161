
import pandas as pd

# Sample DataFrame
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'), 
    (1, '2014-03-01'), 
    (1, '2014-04-01'), 
    (1, '2014-05-01')
], names=['app', 'regmonth'])

df = pd.DataFrame(data, index=index)

# Transforming to percentual values based on the diagonal
percent_df = df.copy()

for i in range(len(percent_df)):
    for j in range(len(percent_df.columns)):
        if i == j:  # Diagonal entries
            percent_df.iat[i, j] = 1
        else:
            diagonal_value = df.iat[i, i]
            if diagonal_value != 0:  # Avoid division by zero
                percent_df.iat[i, j] = df.iat[i, j] / diagonal_value
            else:
                percent_df.iat[i, j] = 0

# Display result
print(percent_df)
