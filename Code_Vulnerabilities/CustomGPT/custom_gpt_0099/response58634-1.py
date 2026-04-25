
values = [['1', '2', '3'], ['4', '5'], ['6', '7', '8', '9']]

# Convert all strings to integers in a single line
newVals = [[int(x) for x in row] for row in values]

print(newVals)
