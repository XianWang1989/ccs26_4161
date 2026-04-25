
import pandas as pd

# Sample multi-index DataFrame
arrays = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    pd.date_range(start='2014-02-01', periods=4, freq='MS').repeat(4)
]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=['app', 'regmonth'])
data = [
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584]
]
df = pd.DataFrame(data, index=index, columns=pd.date_range(start='2014-02-01', periods=4, freq='MS'))

# Calculate percentage based on diagonal values
def transform_to_percentage(df):
    result = df.copy()
    for i, date in enumerate(df.columns):
        diagonal_value = df.xs(i, level='app').loc[(slice(None), date)].values[0]
        result.iloc[:, i] = df.iloc[:, i] / diagonal_value if diagonal_value != 0 else 0
    return result

# Transform DataFrame
percent_df = transform_to_percentage(df)

print(percent_df)
