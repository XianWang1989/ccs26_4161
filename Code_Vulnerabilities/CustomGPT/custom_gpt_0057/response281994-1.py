
import pandas as pd

# Sample data
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584]
}

index = pd.MultiIndex.from_tuples([
    (1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')
], names=['app', 'regmonth'])

df = pd.DataFrame(data, index=index)

# Transforming to percentual values
def transform_to_percent(df):
    diagonal = df.xs(df.index[0], level='regmonth', axis=0).values.flatten()
    return df.div(diagonal, axis=0)

percent_df = transform_to_percent(df)

# Display the transformed DataFrame
print(percent_df)
