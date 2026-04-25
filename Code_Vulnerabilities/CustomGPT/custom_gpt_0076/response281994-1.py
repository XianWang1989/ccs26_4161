
import pandas as pd

# Sample multi-index DataFrame
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

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Function to transform DataFrame to percentual values
def transform_to_percentage(df):
    transformed_df = df.copy()
    for i in range(len(df)):
        diagonal_value = df.iloc[i, i]
        if diagonal_value > 0:
            transformed_df.iloc[i] = df.iloc[i] / diagonal_value
    return transformed_df

# Transform and display the resulting DataFrame
percentual_df = transform_to_percentage(df)
print("\nTransformed DataFrame (Percentual Values):")
print(percentual_df)
