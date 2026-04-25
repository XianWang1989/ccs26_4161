
import pandas as pd

# Create the MultiIndex DataFrame from your data
index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01'),
], names=['app', 'regmonth'])

data = [
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584],
]

df = pd.DataFrame(data, index=index, columns=pd.to_datetime([
    '2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01'
]))
df.columns.name = 'loginsmonth'
df = df.rename_axis(columns='cnt')

# Calculate the new DataFrame
percent_df = df.copy()
for i in range(len(df)):
    diag_value = df.iloc[i, i]
    if diag_value != 0:
        percent_df.iloc[i] = df.iloc[i] / diag_value
    else:
        percent_df.iloc[i] = 0  # or keep it as is, depending on your preference

# Optional: Format the values as strings
percent_df = percent_df.applymap(lambda x: f"{x:.2f}" if x != 0 else "0")

print(percent_df)
