
import pandas as pd

# Create the multiIndex DataFrame
arrays = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01',
                    '2014-03-01', '2014-04-01', '2014-05-01', '2014-05-01'])
]
index = pd.MultiIndex.from_arrays(arrays, names=['app', 'regmonth'])
data = [[6069, 1837, 107, 54],
        [0, 10742, 2709, 1387],
        [0, 0, 5584, 1103],
        [0, 0, 0, 5584]]
df = pd.DataFrame(data, index=index, columns=pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01']))
df.columns.name = 'loginsmonth'

# Calculate the diagonal values
diagonal_values = df.xs(df.index[0], level='regmonth', drop_level=False)['cnt'].values

# Function to calculate the percentual values
def calculate_percentage(row):
    regmonth = row.name[1]
    diagonal_value = df.xs(regmonth, level='regmonth')['cnt'].values[0]
    return row / diagonal_value if diagonal_value != 0 else 0

# Apply the function to each row in the DataFrame
percent_df = df.apply(calculate_percentage)

# Format the DataFrame to show as percentages
percent_df = percent_df.astype(float).round(6)  # Optional: round to 6 decimal places if needed

print(percent_df)
