
# List Assignment
list_assignment = [1, 2]
[x, y] = list_assignment
print(f"List Assignment: x = {x}, y = {y}")

# Tuple Assignment
tuple_assignment = (3, 4)
a, b = tuple_assignment
print(f"Tuple Assignment: a = {a}, b = {b}")

# Demonstrating Mutability
list_example = [1, 2, 3]
list_example[0] = 10  # This works since lists are mutable
print(f"Updated List: {list_example}")

# Demonstrating Immutability
tuple_example = (1, 2, 3)
try:
    tuple_example[0] = 10  # This raises a TypeError
except TypeError as e:
    print(f"Error: {e}")
