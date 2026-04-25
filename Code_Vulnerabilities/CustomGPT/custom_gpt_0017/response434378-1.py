
import pandas as pd

# Sample DataFrame
data = {
    'app_id': [1, 2, 3, 4],
    'reader': ['book1', None, 'book3', 'book4']
}
apps = pd.DataFrame(data)

# Sample boolean Series for filtering
group_indexes = pd.Series([True, False, True, True])

# Filtering and checking for non-null values
non_null_readers = apps[group_indexes]['reader'].notnull()

print(non_null_readers)
