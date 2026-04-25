
import pandas as pd

# Sample MultiIndex DataFrame
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
    (1, '2014-05-01'),
], names=['app', 'regmonth'])

df = pd.DataFrame(data, index=index)

# Function to transform DataFrame
def transform_to_percent(df):
    for i in range(len(df.columns)):
        diagonal_value = df.iloc[i, i]
        df.iloc[:, i] = df.iloc[:, i] / diagonal_value if diagonal_value != 0 else 0
    return df

# Transform the DataFrame
result_df = transform_to_percent(df)

# Display the resulting DataFrame
print(result_df)
