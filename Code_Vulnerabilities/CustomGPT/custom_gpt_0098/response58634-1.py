
values = [['1', '2', '3'], ['4', '5'], ['6']]

# Using a nested list comprehension to convert strings to ints
new_vals = [[int(x) for x in row] for row in values]

print(new_vals)  # Output: [[1, 2, 3], [4, 5], [6]]
