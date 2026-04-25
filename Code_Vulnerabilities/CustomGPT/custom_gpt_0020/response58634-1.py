
# Sample list of lists with strings
values = [['1', '2', '3'], ['4', '5'], ['6', '7', '8', '9']]

# One-liner to convert all string elements to integers
newVals = [int(x) for row in values for x in row]

# Output the result
print(newVals)
