
import pandas as pd

# Sample data
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')
], names=['app', 'regmonth'])

# Create the DataFrame
df = pd.DataFrame(data, index=index)

# Extract diagonal values
diagonal = df['cnt'].values.flatten()[::len(df)//4]

# Transform into percentages
percent_df = df.copy()
for i in range(len(percent_df)):
    percent_df.iloc[i] = df.iloc[i] / diagonal[i]

# Display the transformed DataFrame
print(percent_df)
