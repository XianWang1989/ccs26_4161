import pandas as pd

# Sample DataFrame
data = {
    'app': ['App1', 'App2', 'App3', 'App4'],
    'reader': ['Alice', None, 'Charlie', None]
}
apps = pd.DataFrame(data)

# Create a boolean Series
group_indexes = pd.Series([True, False, True, False])
