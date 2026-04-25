
import pandas as pd

# Sample DataFrame
data = {
    'reader': [None, 'Alice', 'Bob', None, 'Charlie'],
    'score': [85, 90, 70, 88, 95]
}
apps = pd.DataFrame(data)

# Example boolean Series
group_indexes = pd.Series([True, False, True, False, True], index=apps.index)

# Filtering and checking not null
result = apps[group_indexes]['reader'].notnull()

print(result)
