
import pandas as pd

# Sample data
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

# Function to transform the DataFrame
def transform_to_percentage(df):
    # Get the diagonal values
    diagonal = df.xs("cnt", axis=1, level=0).values.diagonal()
    # Calculate percentage
    percent_df = df.xs("cnt", axis=1, level=0) / diagonal[:, None]

    # Reconstruct the DataFrame with the same MultiIndex
    df_percent = pd.concat([percent_df], axis=1)
    df_percent.columns = pd.MultiIndex.from_product([['cnt'], df.columns.levels[1]])

    return df_percent

# Transform the DataFrame
df_percent = transform_to_percentage(df)
print(df_percent)
