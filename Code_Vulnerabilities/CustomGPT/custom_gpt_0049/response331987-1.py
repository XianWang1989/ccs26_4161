
# List assignment
list_assignment = [1, 2]  # Defining a list
[a, b] = list_assignment  # Assigning values from the list to variables
print(f"List Assignment - a: {a}, b: {b}")  # Output: a: 1, b: 2

# Tuple assignment
tuple_assignment = (3, 4)  # Defining a tuple
x, y = tuple_assignment  # Assigning values from the tuple to variables
print(f"Tuple Assignment - x: {x}, y: {y}")  # Output: x: 3, y: 4

# Modifying the list (mutable)
list_assignment[0] = 10
print(f"Modified List Assignment: {list_assignment}")  # Output: [10, 2]

# Trying to modify tuple (immutable) will raise an error
# tuple_assignment[0] = 10  # Uncommenting this line would raise a TypeError
