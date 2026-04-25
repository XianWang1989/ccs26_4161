
# Sample 2D list of strings
values = [["1", "2", "3"], ["4", "5"], ["6", "7", "8", "9"]]

# Convert strings to integers
newVals = [[int(x) for x in row] for row in values]

print(newVals)
