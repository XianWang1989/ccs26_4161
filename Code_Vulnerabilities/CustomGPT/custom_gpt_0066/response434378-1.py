
import pandas as pd

# Sample DataFrame
data = {
    'name': ['app1', 'app2', 'app3', 'app4'],
    'reader': [None, 'reader2', None, 'reader4']
}
apps = pd.DataFrame(data)

# Boolean Series representing which rows to select
group_indexes = pd.Series([True, False, True, False])

# Interacting with the DataFrame
result = apps[group_indexes]['reader'].notnull()

print(result)
