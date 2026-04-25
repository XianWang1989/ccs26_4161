
import pandas as pd

# Constructing the initial DataFrame
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

# Get the diagonal elements
diagonal = df.xs('cnt', axis=1, level=0).values.diagonal()

# Normalize the DataFrame
normalized_df = df.copy()
for i, date in enumerate(df.columns):
    normalized_df[date] = df[date] / diagonal[i]

# Display the result
print(normalized_df)
