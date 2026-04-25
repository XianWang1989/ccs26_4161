
import pandas as pd

# Sample data
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584],
}

index = pd.MultiIndex.from_product([[1], pd.date_range('2014-02-01', '2014-05-01', freq='MS')])
df = pd.DataFrame(data, index=index)

# Function to transform the DataFrame
def transform_to_percent(df):
    # Get diagonal values
    diagonal_values = df.values.diagonal()

    # Create a new DataFrame with percentual values
    percent_df = df.copy()
    for i in range(len(diagonal_values)):
        percent_df.iloc[i] = df.iloc[i] / diagonal_values[i] if diagonal_values[i] != 0 else 0

    return percent_df

# Apply the transformation
percent_df = transform_to_percent(df)

# Display the resulting DataFrame
print(percent_df)
