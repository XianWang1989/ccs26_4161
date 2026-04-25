
values = [['1', '2', '3'], ['4', '5'], ['6']]

# Using a one-liner to convert strings to integers
new_vals = [int(x) for row in values for x in row]

print(new_vals)
