
import pandas as pd

# Sample DataFrame
data = {
    'reader': [None, 'Alice', 'Bob', None, 'Charlie'],
    'value': [1, 2, 3, 4, 5]
}
apps = pd.DataFrame(data)

# Boolean Series indicating which rows to include
group_indexes = pd.Series([True, False, True, False, True], index=apps.index)

# Applying boolean indexing and checking for non-null values in 'reader'
result = apps[group_indexes]['reader'].notnull()

print(result)
