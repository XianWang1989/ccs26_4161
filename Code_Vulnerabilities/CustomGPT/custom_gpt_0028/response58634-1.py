
values = [['1', '2', '3'], ['4', '5'], ['6', '7', '8', '9']]

# Convert strings to integers using a nested list comprehension
new_vals = [[int(x) for x in row] for row in values]

print(new_vals)
