
import pandas as pd
import numpy as np

# Sample data
data = {
    ("cnt", "2014-02-01"): [6069, 0, 0, 0],
    ("cnt", "2014-03-01"): [1837, 10742, 0, 0],
    ("cnt", "2014-04-01"): [107, 2709, 5584, 0],
    ("cnt", "2014-05-01"): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_tuples(
    [(1, "2014-02-01"), (1, "2014-03-01"), (1, "2014-04-01"), (1, "2014-05-01")]
)
df = pd.DataFrame(data, index=index)

# Function to transform to percentages relative to the diagonal
def transform_to_percent(df):
    # Extract diagonal values
    diagonal = np.diag(df.values)
    percent_df = df.div(diagonal, axis=0)
    return percent_df

# Apply transformation
result_df = transform_to_percent(df)

print(result_df)
