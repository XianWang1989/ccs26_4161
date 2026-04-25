
import pandas as pd

# Sample DataFrame
data = {
    'reader': [None, 'Alice', 'Bob', None, 'Charlie'],
    'score': [85, 92, 88, 75, 95],
}

apps = pd.DataFrame(data)

# Sample boolean Series
group_indexes = pd.Series([True, False, True, False, True])

# Applying the boolean indexing and checking for not null
result = apps[group_indexes]['reader'].notnull()

print(result)
