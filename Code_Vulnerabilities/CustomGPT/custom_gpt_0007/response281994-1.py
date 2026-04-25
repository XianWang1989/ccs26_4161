
import pandas as pd

# Sample data creation
data = {
    ('cnt', 'loginsmonth'): [
        [6069, 1837, 107, 54],
        [0, 10742, 2709, 1387],
        [0, 0, 5584, 1103],
        [0, 0, 0, 5584]
    ]
}
index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')],
    names=['app', 'regmonth']
)
df = pd.DataFrame(data[('cnt', 'loginsmonth')], index=index, columns=['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01'])

# Transform the DataFrame to percentage of diagonal values
result = df.copy()

# Iterate over the rows and calculate the percentage values
for i in range(len(df)):
    diagonal_value = df.iloc[i, i]  # Taking the diagonal value
    if diagonal_value != 0:  # Avoid division by zero
        result.iloc[i] = df.iloc[i] / diagonal_value

# Display the result
print(result)
