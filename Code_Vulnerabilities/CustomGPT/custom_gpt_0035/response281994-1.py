
import pandas as pd

# Sample DataFrame creation
index = pd.MultiIndex.from_tuples([(1, '2014-02-01'), (1, '2014-03-01'), 
                                    (1, '2014-04-01'), (1, '2014-05-01')],
                                   names=['app', 'regmonth'])
data = [[6069, 1837, 107, 54],
        [0, 10742, 2709, 1387],
        [0, 0, 5584, 1103],
        [0, 0, 0, 5584]]
columns = pd.date_range('2014-02-01', periods=4, freq='MS')
df = pd.DataFrame(data, index=index, columns=columns)

# Transforming to percentage values relative to diagonal
for i in range(len(df)):
    diagonal_value = df.iloc[i, i]  # Get diagonal element
    if diagonal_value > 0:  # Avoid division by zero
        df.iloc[i] = df.iloc[i] / diagonal_value

# Display the transformed DataFrame
print(df)
