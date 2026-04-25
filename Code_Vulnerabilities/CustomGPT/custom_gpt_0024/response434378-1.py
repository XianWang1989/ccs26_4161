
import pandas as pd

# Sample DataFrame
data = {
    'reader': [None, 'Alice', 'Bob', None, 'Charlie'],
    'score': [85, 90, 78, None, 95]
}
apps = pd.DataFrame(data)

# Sample boolean Series for indexing
group_indexes = pd.Series([True, False, True, False, True])

# Filtering and checking for not null values in 'reader'
result = apps[group_indexes]['reader'].notnull()

print(result)
