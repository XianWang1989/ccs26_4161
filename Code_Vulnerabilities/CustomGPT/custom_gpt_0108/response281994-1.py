
import pandas as pd

# Sample data
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584],
}
index = pd.MultiIndex.from_tuples([(1, '2014-02-01'), (1, '2014-03-01'), 
                                    (1, '2014-04-01'), (1, '2014-05-01')],
                                   names=['app', 'regmonth'])

df = pd.DataFrame(data, index=index)

# Function to convert to percentage of diagonal values
def transform_to_percentage(df):
    # Extract the diagonal values
    diag_values = df.xs(df.index[0], level='regmonth', axis=0)['cnt'].values

    # Create a new DataFrame for percentages
    percentage_df = df.copy()

    for i, col in enumerate(df.columns):
        percentage_df[col] = df[col] / diag_values[i]

    return percentage_df

# Transform the DataFrame
result_df = transform_to_percentage(df)

# Display the result
print(result_df)
