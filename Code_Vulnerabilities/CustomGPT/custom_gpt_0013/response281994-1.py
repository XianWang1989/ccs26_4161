
import pandas as pd

# Sample data creation
data = {
    ("cnt", "2014-02-01"): [6069, 0, 0, 0],
    ("cnt", "2014-03-01"): [1837, 10742, 0, 0],
    ("cnt", "2014-04-01"): [107, 2709, 5584, 0],
    ("cnt", "2014-05-01"): [54, 1387, 1103, 5584]
}
index = pd.MultiIndex.from_tuples(
    [(1, "2014-02-01"), (1, "2014-03-01"), (1, "2014-04-01"), (1, "2014-05-01")],
    names=["app", "regmonth"]
)
df = pd.DataFrame(data, index=index)

# Function to transform DataFrame
def transform_to_percentage(df):
    # Get diagonal values
    diagonal_values = df.xs(df.index[0][1], level=1, axis=0)

    # Calculate percentage
    for i in range(len(df)):
        df.iloc[i] = df.iloc[i] / diagonal_values.iloc[i]

    return df

# Apply transformation
result_df = transform_to_percentage(df)

# Display the transformed DataFrame
print(result_df)
