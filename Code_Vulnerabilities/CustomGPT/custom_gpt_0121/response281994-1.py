
import pandas as pd

# Sample data
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

# Create the DataFrame with MultiIndex
index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'), 
     (1, '2014-03-01'), 
     (1, '2014-04-01'), 
     (1, '2014-05-01')],
    names=['app', 'regmonth']
)

df = pd.DataFrame(data, index=index)

# Function to convert values to percentage of diagonal
def transform_to_percent(df):
    diagonal = df.xs(df.index[0], level=1, axis=0).values  # Extract diagonal values
    for i, row in enumerate(df.values):
        for j in range(len(row)):
            if diagonal[i] != 0:
                df.iloc[i, j] = row[j] / diagonal[i]  # Compute percentage
    return df

# Transform the DataFrame
transformed_df = transform_to_percent(df)

# Display the transformed DataFrame
print(transformed_df)
