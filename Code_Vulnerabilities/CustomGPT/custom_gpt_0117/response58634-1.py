
values = [['1', '2', '3'], ['4', '5'], ['6']]

# One-liner to convert all strings to ints
newVals = [[int(x) for x in row] for row in values]

print(newVals)
