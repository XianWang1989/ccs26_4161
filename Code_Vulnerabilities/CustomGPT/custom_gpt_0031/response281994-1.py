
import pandas as pd

# Sample data
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'),
    (1, '2014-03-01'),
    (1, '2014-04-01'),
    (1, '2014-05-01')
], names=['app', 'regmonth'])

df = pd.DataFrame(data, index=index)

# Function to calculate percentages
def calculate_percentages(df):
    # Extract the diagonal values
    diagonal_values = df.xs(df.index[0], level='app').values.flatten()

    # Create a new DataFrame for percentages
    percentage_df = df.copy()

    for i, regmonth in enumerate(df.index.levels[1]):
        percentage_df.xs(i, level='app') = df.xs(i, level='app').div(diagonal_values[i])

    return percentage_df

# Calculate percentages
percentage_df = calculate_percentages(df)

# Display the result
print(percentage_df)
