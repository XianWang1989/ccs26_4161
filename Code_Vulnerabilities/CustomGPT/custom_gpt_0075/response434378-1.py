
import pandas as pd

# Sample DataFrame
data = {
    'reader': [None, 'Alice', 'Bob', None, 'Charlie'],
    'score': [85, 90, 88, 95, 80]
}
apps = pd.DataFrame(data)

# Boolean Series for filtering
group_indexes = pd.Series([True, False, True, False, True])

# Use boolean indexing to filter and check for non-null values
result = apps[group_indexes]['reader'].notnull()

print(result)
