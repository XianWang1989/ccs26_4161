
import pandas as pd

# Sample data creation
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')
])

df = pd.DataFrame(data, index=index)

# Calculate percentages
for col in df.columns:
    diagonal_value = df.at[(1, col[1]), col]  # Get the diagonal value
    df[col] = df[col] / diagonal_value  # Divide by the diagonal value

# Display the transformed DataFrame
print(df)
