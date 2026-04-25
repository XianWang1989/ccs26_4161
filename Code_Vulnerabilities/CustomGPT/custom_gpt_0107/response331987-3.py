
# List assignment
list_values = [1, 2, 3]
[a, b] = list_values  # This works fine

# Tuple assignment
tuple_values = (4, 5)
x, y = tuple_values  # This also works fine

# Attempting to assign to a list variable
try:
    [x, y] = (6, 7)  # This works, but if the right side had more than two values, it would raise an error
except ValueError as e:
    print(e)  # Raises ValueError: too many values to unpack (expected 2)

# Showing flexibility
c, d = (8, 9)  # Tuple assignment with tuple
e, f = [10, 11]  # Tuple assignment with list
print(a, b, x, y, c, d, e, f)  # Outputs: 1 2 4 5 8 9 10 11
