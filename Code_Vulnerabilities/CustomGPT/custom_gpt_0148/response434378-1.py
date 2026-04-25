
import pandas as pd

# Sample DataFrame
data = {
    'id': [1, 2, 3, 4],
    'reader': ['A', None, 'C', 'D']
}

apps = pd.DataFrame(data)

# Creating a boolean Series
group_indexes = apps['reader'].notnull()  # True for non-null values in 'reader'

# Using the boolean Series to filter and check non-null values
result = apps[group_indexes]['reader'].notnull()

print(result)
