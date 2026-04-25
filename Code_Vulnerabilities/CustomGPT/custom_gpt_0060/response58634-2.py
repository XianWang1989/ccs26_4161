
values = [['1', '2', '3'], ['4', '5'], ['6']]
newVals = [[int(x) for x in row] for row in values]

print(newVals)  # Output: [[1, 2, 3], [4, 5], [6]]
