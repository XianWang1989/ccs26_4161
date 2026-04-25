
values = [['1', '2', '3'], ['4', '5'], ['6']]

# Convert all strings to integers using a one-liner
new_vals = [int(x) for row in values for x in row]

print(new_vals)  # Output: [1, 2, 3, 4, 5, 6]
