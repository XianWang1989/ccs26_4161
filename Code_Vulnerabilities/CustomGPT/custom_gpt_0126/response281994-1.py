
import pandas as pd

# Example DataFrame creation
data = { 
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'), (1, '2014-03-01'), 
    (1, '2014-04-01'), (1, '2014-05-01')
], names=["app", "regmonth"])

df = pd.DataFrame(data, index=index)

# Transforming to percentage of the diagonal
for col in df.columns:
    diagonal_value = df[col].iloc[0]  # Get the diagonal value (first element in each group)
    df[col] = df[col] / diagonal_value

# Display the transformed DataFrame
print(df)
