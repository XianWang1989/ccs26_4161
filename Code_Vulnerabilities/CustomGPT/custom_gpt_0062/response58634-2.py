
values = [['1', '2'], ['3', '4', '5'], ['6']]
newVals = [int(x) for row in values for x in row]

print(newVals)  # Output: [1, 2, 3, 4, 5, 6]
