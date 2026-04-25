
import pandas as pd

# Sample DataFrame
data = {
    'reader': ['Alice', None, 'Charlie', 'David', 'Eve'],
    'score': [90, 85, 88, 92, 75]
}
apps = pd.DataFrame(data)

# Boolean Series for filtering
group_indexes = pd.Series([True, False, True, False, True])

# Using the boolean index to filter and check for not null
result = apps[group_indexes]['reader'].notnull()

print(result)
