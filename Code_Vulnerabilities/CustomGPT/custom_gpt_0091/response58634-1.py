
values = [['1', '2', '3'], ['4', '5'], ['6', '7', '8', '9']]

# Using nested list comprehension to convert all strings to ints
new_vals = [[int(x) for x in row] for row in values]

print(new_vals)
