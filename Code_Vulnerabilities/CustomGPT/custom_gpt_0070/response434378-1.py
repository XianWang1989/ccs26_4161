
import pandas as pd

# Sample DataFrame
data = {
    'reader': ['Alice', None, 'Charlie', 'David', None],
    'value': [1, 2, 3, 4, 5]
}
apps = pd.DataFrame(data)

# Boolean Series for filtering
group_indexes = pd.Series([True, False, True, False, True])

# Filtering with boolean index and checking for non-null 'reader' values
non_null_readers = apps[group_indexes]['reader'].notnull()

# Display results
print(non_null_readers)
