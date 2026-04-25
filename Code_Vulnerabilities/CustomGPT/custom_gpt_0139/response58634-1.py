
values = [['1', '2', '3'], ['4', '5'], ['6', '7', '8', '9']]

# Using a single list comprehension to flatten and convert strings to integers
newVals = [int(x) for row in values for x in row]

print(newVals)
