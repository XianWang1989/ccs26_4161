
# Assuming you have already created an instance of Recipe
r = Recipe(id=1, title="Pasta", instructions="Boil water, add pasta.")

# To access the nth column value
n = 2  # For instance, to get the instructions
columns = list(r.__dict__.keys())
nth_column_value = r.__dict__[columns[n]]

print(nth_column_value)  # Output: Boil water, add pasta.
