
import pandas as pd

# Sample multiIndex DataFrame
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_product([[1], pd.date_range(start='2014-02-01', periods=4, freq='MS')],
                                    names=['app', 'regmonth'])
df = pd.DataFrame(data, index=index)

# Calculate the diagonal values
diagonal_values = df.xs(df.index[0], level=0)

# Transform values to percent relative to the diagonal
percent_df = df.div(diagonal_values.values, axis=1)

# Display the transformed DataFrame
print(percent_df)
