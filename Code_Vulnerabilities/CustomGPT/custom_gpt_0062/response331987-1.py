
# List assignment
list_assignment = [1, 2]
a, b = list_assignment  # Unpacking the list
print(f"List Assignment: a = {a}, b = {b}")  # Output: a = 1, b = 2

# Modifying the list
list_assignment[0] = 99
print(f"Modified List: {list_assignment}")  # Output: [99, 2]

# Tuple assignment
tuple_assignment = (1, 2)
x, y = tuple_assignment  # Unpacking the tuple
print(f"Tuple Assignment: x = {x}, y = {y}")  # Output: x = 1, y = 2

# Attempting to modify the tuple will result in an error
# tuple_assignment[0] = 99  # Uncommenting this line will raise a TypeError
