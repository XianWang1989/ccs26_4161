
import pandas as pd

# Sample data creation
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

# Function to calculate percentual values
def transform_to_percent(df):
    # Get diagonal values
    diags = df.xs(df.index[0], level=0).values.flatten()
    percent_df = df.copy()

    for i, val in enumerate(diags):
        if val > 0:  # Prevent division by zero
            percent_df.iloc[:, i] = df.iloc[:, i] / val

    return percent_df

# Applying the function
percent_df = transform_to_percent(df)

print(percent_df)
