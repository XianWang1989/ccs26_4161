
values = [['1', '2', '3'], ['4', '5'], ['6', '7', '8', '9']]

# One-liner to convert all strings to integers in a flattened manner
newVals = [int(x) for row in values for x in row]

print(newVals)
