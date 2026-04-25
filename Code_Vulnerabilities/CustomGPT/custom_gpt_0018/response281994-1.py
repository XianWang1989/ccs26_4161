
import pandas as pd

# Sample data creation
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}
index = pd.MultiIndex.from_product([[1], pd.to_datetime(['2014-02-01', '2014-03-01', '2014-04-01', '2014-05-01'])], names=['app', 'regmonth'])
df = pd.DataFrame(data, index=index)

# Function to calculate percentages
def transform_to_percent(df):
    # Get the diagonal values (i.e., the first value for each 'app' across the months)
    diagonal = df.xs(key=pd.IndexSlice[:, pd.IndexSlice[:, df.index.levels[1]]], axis=0, level=0)

    # Transform the DataFrame
    for col in df.columns:
        df.loc[:, col] = df.loc[:, col] / diagonal[col]

    return df

# Transforming the DataFrame
transformed_df = transform_to_percent(df)

# Display the transformed DataFrame
print(transformed_df)
