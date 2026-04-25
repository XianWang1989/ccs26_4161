
# List assignment
list_assignment = [1, 2]
[a, b] = list_assignment
print(f"List assignment: a = {a}, b = {b}")  # Output: a = 1, b = 2

# Tuple assignment
tuple_assignment = (1, 2)
a, b = tuple_assignment
print(f"Tuple assignment: a = {a}, b = {b}")  # Output: a = 1, b = 2

# Demonstrating mutability
my_list = [1, 2, 3]
my_list[0] = 99  # This works
print(my_list)  # Output: [99, 2, 3]

# Trying to modify a tuple will result in an error
my_tuple = (1, 2, 3)
# my_tuple[0] = 99  # This would raise a TypeError
