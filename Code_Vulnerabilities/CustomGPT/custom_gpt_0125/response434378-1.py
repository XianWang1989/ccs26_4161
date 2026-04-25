
import pandas as pd

# Sample DataFrame
data = {
    'reader': ['Book A', None, 'Book C', 'Book D', None],
    'author': ['Author 1', 'Author 2', 'Author 3', 'Author 4', 'Author 5']
}
apps = pd.DataFrame(data)

# Boolean Series indicating which rows to select
group_indexes = apps['reader'].notnull()

# Using the boolean indexer to filter the 'reader' column
filtered_readers = apps[group_indexes]['reader']

print(filtered_readers)
