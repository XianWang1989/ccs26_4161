
import pandas as pd

# Sample DataFrame
data = {
    ('loginsmonth', '2014-02-01'): [6069, 0, 0, 0],
    ('loginsmonth', '2014-03-01'): [1837, 10742, 0, 0],
    ('loginsmonth', '2014-04-01'): [107, 2709, 5584, 0],
    ('loginsmonth', '2014-05-01'): [54, 1387, 1103, 5584],
}

index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')],
    names=['app', 'regmonth']
)

df = pd.DataFrame(data, index=index)

# Transforming to percentage relative to diagonal
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        diagonal_value = df.iloc[i, i]  # Get the diagonal value
        if diagonal_value != 0:  # Avoid division by zero
            df.iloc[i, j] = df.iloc[i, j] / diagonal_value

# Converting to percentage format
df = df.applymap(lambda x: f'{x:.2%}')

print(df)
