
import pandas as pd

# Sample data creation
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
    (1, '2014-05-01'),
], names=['app', 'regmonth'])

df = pd.DataFrame(data, index=index)

# Normalize the values relative to the diagonal
def transform_to_percentage(group):
    diagonal_value = group.iloc[0, 0]  # Get the diagonal value
    return group / diagonal_value if diagonal_value != 0 else group

# Apply the transformation
result = df.groupby(level=0, axis=0).apply(transform_to_percentage)

# Display the result
print(result)
