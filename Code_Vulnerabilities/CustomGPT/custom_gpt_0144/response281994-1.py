import pandas as pd

# Example DataFrame setup
index = pd.MultiIndex.from_product([[1], pd.date_range('2014-02-01', periods=4, freq='MS')], names=['app', 'regmonth'])
columns = pd.date_range('2014-02-01', periods=4, freq='MS', name='loginsmonth')
data = [
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584],
]
df = pd.DataFrame(data, index=index, columns=columns)
df.columns.name = 'loginsmonth'

# Calculate diagonal values for each row
diagonal_values = df.lookup(df.index, df.columns[:len(df)])

# Divide each row by its diagonal
percent_df = df.div(diagonal_values, axis=0)

# Optional: format as fractions
formatted_df = df.astype(str) + '/' + pd.DataFrame(diagonal_values[:, None], index=df.index, columns=df.columns).astype(str)

print(formatted_df)
