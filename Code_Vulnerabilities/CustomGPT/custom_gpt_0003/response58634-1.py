
values = [['1', '2', '3'], ['4', '5'], ['6']]

# Using nested list comprehension to convert strings to integers
newVals = [int(x) for row in values for x in row]

print(newVals)  # Output will be: [1, 2, 3, 4, 5, 6]
