
import pandas as pd

# Sample data
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')],
    names=['app', 'regmonth']
)
df = pd.DataFrame(data, index=index)

# Function to transform dataframe
def transform_to_percent(df):
    # Iterate through the rows and compute percentage based on the diagonal
    for i in range(len(df)):
        diag_value = df.iloc[i].loc[:, 'cnt'].iloc[i]
        df.iloc[i] = df.iloc[i] / diag_value
    return df

# Transforming the DataFrame
transformed_df = transform_to_percent(df)

# Displaying the result
print(transformed_df)
