
# Assuming r is an instance of Recipe
r = Recipe(id=1, title="Pasta", instructions="Boil water")

# Get the n-th column value
print(get_nth_column(r, 0))  # Output: 1
print(get_nth_column(r, 1))  # Output: "Pasta"
print(get_nth_column(r, 2))  # Output: "Boil water"
