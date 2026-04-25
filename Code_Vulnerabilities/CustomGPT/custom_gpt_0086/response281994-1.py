
import pandas as pd

# Sample data
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}
index = pd.MultiIndex.from_tuples([(1, '2014-02-01'), (1, '2014-03-01'), 
                                    (1, '2014-04-01'), (1, '2014-05-01')])
df = pd.DataFrame(data, index=index)

# Function to calculate percentage
def transform_to_percentage(df):
    # Get the diagonal values
    diagonal_values = df.xs('2014-02-01', level='regmonth', axis=0).to_numpy().flatten()
    perc_df = df.copy()

    for i, col in enumerate(df.columns):
        if i < len(diagonal_values):
            perc_df[col] = df[col] / diagonal_values[i]

    return perc_df

# Transform the DataFrame
transformed_df = transform_to_percentage(df)

# Displaying the transformed DataFrame
print(transformed_df)
