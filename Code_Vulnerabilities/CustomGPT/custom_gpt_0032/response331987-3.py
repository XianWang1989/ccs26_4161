
# List assignment
list_assignment = [1, 2]
[a, b] = list_assignment
print(f"List assignment: a = {a}, b = {b}")

# Tuple assignment
tuple_assignment = (1, 2)
a, b = tuple_assignment
print(f"Tuple assignment: a = {a}, b = {b}")

# Demonstrating mutability
my_list = [1, 2, 3]
my_list[0] = 10
print(f"Modified list: {my_list}")

# Attempting to modify a tuple (this will raise an error)
my_tuple = (1, 2, 3)
try:
    my_tuple[0] = 10
except TypeError as e:
    print(f"Error: {e}")
