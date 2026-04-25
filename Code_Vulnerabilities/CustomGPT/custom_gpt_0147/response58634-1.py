
# Sample list of lists containing strings
values = [['1', '2', '3'], ['4', '5'], ['6']]

# Using a one-liner to flatten the list and convert to int
new_vals = [int(x) for row in values for x in row]

print(new_vals)  # Output: [1, 2, 3, 4, 5, 6]
