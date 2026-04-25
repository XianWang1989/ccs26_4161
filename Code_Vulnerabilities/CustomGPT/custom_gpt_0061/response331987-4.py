
# List assignment
[a, b] = [1, 2]
print(f"List assignment: a = {a}, b = {b}")

# Tuple assignment
a, b = (1, 2)
print(f"Tuple assignment: a = {a}, b = {b}")

# Demonstrating mutability
my_list = [1, 2]
my_list[0] = 42
print(f"Modified list: {my_list}")

my_tuple = (1, 2)
# Uncommenting the next line will cause an error
# my_tuple[0] = 42  # TypeError: 'tuple' object does not support item assignment
