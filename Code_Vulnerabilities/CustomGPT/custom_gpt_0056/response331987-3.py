
# List Assignment
list_assigned = [1, 2]
[a, b] = list_assigned
print(f"List Assignment: a={a}, b={b}")  # Output: a=1, b=2

# Tuple Assignment
tuple_assigned = (3, 4)
x, y = tuple_assigned
print(f"Tuple Assignment: x={x}, y={y}")  # Output: x=3, y=4

# Demonstrating mutability
list_example = [1, 2, 3]
list_example[0] = 10  # This works because lists are mutable
print(f"Modified List: {list_example}")  # Output: [10, 2, 3]

# Attempting to modify a tuple
tuple_example = (1, 2, 3)
# tuple_example[0] = 10  # Uncommenting this line would raise a TypeError
