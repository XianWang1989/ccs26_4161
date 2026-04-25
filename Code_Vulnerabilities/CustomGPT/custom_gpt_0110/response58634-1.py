
# Example input: a list of lists of strings
values = [["1", "2", "3"], ["4", "5"], ["6", "7", "8", "9"]]

# One-liner to convert all strings to integers
newVals = [int(x) for row in values for x in row]

print(newVals)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
