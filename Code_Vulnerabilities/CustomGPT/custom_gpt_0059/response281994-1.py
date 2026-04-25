
import pandas as pd
import numpy as np

# Sample multiindex DataFrame
index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')],
    names=['app', 'regmonth']
)
columns = pd.MultiIndex.from_tuples(
    [('cnt', '2014-02-01'), ('cnt', '2014-03-01'), ('cnt', '2014-04-01'), ('cnt', '2014-05-01')],
    names=['loginsmonth', 'date']
)
data = [
    [6069, 1837, 107, 54],
    [0, 10742, 2709, 1387],
    [0, 0, 5584, 1103],
    [0, 0, 0, 5584]
]
df = pd.DataFrame(data, index=index, columns=columns)

# Function to transform to percentual values
def convert_to_percent(df):
    result = df.copy()
    diagonal = np.diag(df.values)

    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            if diagonal[i] != 0:
                result.iloc[i, j] = df.iloc[i, j] / diagonal[i]
            else:
                result.iloc[i, j] = 0  # Avoid division by zero

    return result

# Transform the DataFrame
percent_df = convert_to_percent(df)

print(percent_df)
