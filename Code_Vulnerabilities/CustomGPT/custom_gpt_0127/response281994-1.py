
import pandas as pd

# Sample multi-index DataFrame creation
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}
index = pd.MultiIndex.from_tuples([(1, '2014-02-01'), 
                                    (1, '2014-03-01'),
                                    (1, '2014-04-01'),
                                    (1, '2014-05-01')],
                                   names=['app', 'regmonth'])
df = pd.DataFrame(data, index=index)

# Accessing diagonal values
diagonal_values = df.xs(key=df.index.levels[1][0], level='regmonth')

# Transforming DataFrame to percentage values
percent_df = df.copy()
for col in df.columns:
    diagonal_value = diagonal_values[col].iloc[0]
    percent_df[col] = df[col] / diagonal_value if diagonal_value != 0 else 0

# Display the transformed DataFrame
print(percent_df)
