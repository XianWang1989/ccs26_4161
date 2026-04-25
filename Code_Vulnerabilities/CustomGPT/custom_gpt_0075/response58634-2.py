
values = [['1', '2'], ['3', '4']]
new_vals = [int(x) for row in values for x in row]
print(new_vals)  # Output: [1, 2, 3, 4]
