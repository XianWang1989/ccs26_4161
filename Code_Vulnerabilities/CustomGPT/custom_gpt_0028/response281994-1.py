
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

# Function to transform to percentage
def transform_to_percentage(df):
    # Get the diagonal values
    diagonal = df.xs(df.index[0][1], level='regmonth', axis=0)

    # Create an empty DataFrame to store the results
    result = pd.DataFrame(index=df.index, columns=df.columns)

    for col in df.columns:
        for i in range(len(df)):
            regmonth_value = df.iloc[i][col]
            diagonal_value = diagonal[col]
            if diagonal_value != 0:  # Avoid division by zero
                percent_value = regmonth_value / diagonal_value
                result.iloc[i][col] = percent_value
            else:
                result.iloc[i][col] = 0  # Handle zero case

    return result

# Transform the DataFrame
percent_df = transform_to_percentage(df)

# Display the transformed DataFrame
print(percent_df)
