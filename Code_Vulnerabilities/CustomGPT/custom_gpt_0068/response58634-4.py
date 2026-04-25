
# Sample 2D list of strings
values = [["1", "2", "3"], ["4", "5"], ["6", "7", "8", "9"]]

# Flatten and convert to integers
newVals = [int(x) for row in values for x in row]

print(newVals)
