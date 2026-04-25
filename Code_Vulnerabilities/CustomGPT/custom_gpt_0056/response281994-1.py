
import pandas as pd
import numpy as np

# Sample data
data = {
    ('cnt', '2014-02-01'): [6069, 0, 0, 0],
    ('cnt', '2014-03-01'): [1837, 10742, 0, 0],
    ('cnt', '2014-04-01'): [107, 2709, 5584, 0],
    ('cnt', '2014-05-01'): [54, 1387, 1103, 5584],
}
index = pd.MultiIndex.from_tuples(
    [(1, '2014-02-01'), (1, '2014-03-01'), (1, '2014-04-01'), (1, '2014-05-01')], 
    names=['app', 'regmonth']
)
df = pd.DataFrame(data, index=index)

# Extracting diagonal values
diagonal = df.stack().unstack(level=0).values.diagonal()
diagonal = np.tile(diagonal[:, np.newaxis], (1, df.shape[1]))

# Transforming to percent values
percent_df = df / diagonal

# Display the transformed DataFrame
print(percent_df)
