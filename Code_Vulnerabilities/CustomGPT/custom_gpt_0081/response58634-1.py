
# Example list of lists
values = [['1', '2', '3'], ['4', '5'], ['6', '7', '8', '9']]

# One-liner to convert all strings in the 2D list to integers
newVals = [[int(x) for x in row] for row in values]

print(newVals)  # Output: [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
