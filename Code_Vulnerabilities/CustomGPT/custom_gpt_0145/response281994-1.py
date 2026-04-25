
import pandas as pd

# Create a sample multi-index DataFrame
index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'),
    (1, '2014-03-01'),
    (1, '2014-04-01'),
    (1, '2014-05-01'),
], names=['app', 'regmonth'])

data = {
    'loginsmonth': ['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01'],
    'cnt': [
        [6069, 1837, 107, 54],
        [0, 10742, 2709, 1387],
        [0, 0, 5584, 1103],
        [0, 0, 0, 5584],
    ]
}

# Creating the DataFrame
df = pd.DataFrame(data['cnt'], index=index, columns=pd.to_datetime(data['loginsmonth']))

# Transform the DataFrame
for i in range(len(df)):
    diagonal_value = df.iloc[i, i]  # Get the diagonal value
    if diagonal_value != 0:  # Avoid division by zero
        df.iloc[i] = df.iloc[i] / diagonal_value

# Display the transformed DataFrame
print(df)
