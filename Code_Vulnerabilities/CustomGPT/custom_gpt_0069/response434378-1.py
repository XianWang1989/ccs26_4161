
import pandas as pd

# Sample data
data = {
    'app_name': ['App A', 'App B', 'App C', 'App D'],
    'reader': [None, 'pdf', 'epub', None]
}

# Creating DataFrame
apps = pd.DataFrame(data)

# Creating a boolean Series for filtering
group_indexes = apps['reader'].notnull()  # True for rows where 'reader' is not null

# Applying the boolean indexing and checking non-null values in 'reader'
non_null_readers = apps[group_indexes]['reader'].notnull()

print(non_null_readers)
