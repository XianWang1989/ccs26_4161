
import pandas as pd

# Sample DataFrame
data = {
    'reader': [1, None, 3, None, 5],
    'name': ['A', 'B', 'C', 'D', 'E']
}
apps = pd.DataFrame(data)

# Boolean Series indicating which rows to select
group_indexes = pd.Series([True, False, True, False, True])

# Using boolean indexing and checking for not-null values
result = apps[group_indexes]['reader'].notnull()

print(result)
