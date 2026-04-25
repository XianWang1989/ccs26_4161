
import pandas as pd

# Sample DataFrame
data = {
    'app_name': ['App A', 'App B', 'App C', 'App D'],
    'reader': ['Text', None, 'Text', None],
    'rating': [4.5, 3.0, 4.8, 2.5]
}

apps = pd.DataFrame(data)

# Sample boolean Series (simulate a condition)
group_indexes = pd.Series([True, False, True, False])

# Filtering the DataFrame
result = apps[group_indexes]['reader'].notnull()

# Displaying the result
print(result)
