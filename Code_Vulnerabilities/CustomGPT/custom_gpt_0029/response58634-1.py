
values = [['1', '2', '3'], ['4', '5', '6'], ['7']]

# Convert all strings in a 2D list to integers
newVals = [[int(x) for x in row] for row in values]

print(newVals)
