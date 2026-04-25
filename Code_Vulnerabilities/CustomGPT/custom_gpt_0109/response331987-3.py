
# List Assignment
list_values = [1, 2]
[a, b] = list_values
print(f"List Assignment: a = {a}, b = {b}")  # Output: a = 1, b = 2

# Tuple Assignment
tuple_values = (3, 4)
c, d = tuple_values
print(f"Tuple Assignment: c = {c}, d = {d}")  # Output: c = 3, d = 4

# Modifying List
list_values[0] = 10
print(f"Modified List: {list_values}")  # Output: [10, 2]

# Attempting to modify Tuple (will raise an error)
# tuple_values[0] = 30  # Uncommenting this line will raise TypeError
