
import pandas as pd

# Creating a sample DataFrame
data = {
    'name': ['app1', 'app2', 'app3', 'app4'],
    'reader': [None, 'PDF Reader', None, 'Ebook Reader'],
    'rating': [4.5, 3.8, None, 5.0]
}

apps = pd.DataFrame(data)

# Example condition for filtering
group_indexes = apps['rating'] > 4.0  # Boolean Series based on ratings

# Applying the boolean Series to filter and check 'reader' column
result = apps[group_indexes]['reader'].notnull()

# Display the result
print(result)
