
import pandas as pd

# Sample multi-index DataFrame
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584],
}
index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'), (1, '2014-03-01'),
    (1, '2014-04-01'), (1, '2014-05-01')
], names=['app', 'regmonth'])

df = pd.DataFrame(data, index=index)

# Transform to percentage of the diagonal
for i in range(len(df)):
    diagonal_value = df.iloc[i, i]  # Get the diagonal value
    if diagonal_value != 0:  # Avoid division by zero
        df.iloc[i, :] = df.iloc[i, :] / diagonal_value

# Optional: Format the DataFrame for clearer readability (optional step)
df = df.applymap(lambda x: f"{x:.2%}")  # Convert to percentage string format

# Display the resulting DataFrame
print(df)
