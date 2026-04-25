
import pandas as pd

# Creating the initial multi-index DataFrame
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

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Transforming to percentage values related to the diagonal
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        if i <= j:  # Diagonal and above
            diagonal_value = df.iloc[i, i]
            df.iloc[i, j] = df.iloc[i, j] / diagonal_value if diagonal_value != 0 else 0

# Display the transformed DataFrame
print("\nTransformed DataFrame (Percentage Values):")
print(df)
