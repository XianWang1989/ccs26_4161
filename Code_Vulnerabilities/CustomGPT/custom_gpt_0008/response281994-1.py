
import pandas as pd

# Sample DataFrame creation
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}
index = pd.MultiIndex.from_tuples([(1, '2014-02-01'), (1, '2014-03-01'), 
                                    (1, '2014-04-01'), (1, '2014-05-01')],
                                   names=['app', 'regmonth'])
df = pd.DataFrame(data, index=index)

# Calculate diagonal values
diagonal = df.xs('2014-02-01', level='regmonth', axis=0, drop_level=False)
for date in df.columns:
    if date != '2014-02-01':
        diagonal = diagonal.append(df.xs(date, level='regmonth', axis=0, drop_level=False))

# Normalize each value by its diagonal
for i, date in enumerate(df.columns):
    df.xs(date, level='regmonth', axis=0, drop_level=False).iloc[:, :] /= df.iloc[i, i]

# Display the transformed DataFrame
print(df)
