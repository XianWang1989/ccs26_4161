
# List assignment
[a, b] = [1, 2]
print(f"List assignment: a = {a}, b = {b}")

# Tuple assignment
a, b = (3, 4)  # Alternatively: a, b = [3, 4]
print(f"Tuple assignment: a = {a}, b = {b}")

# Demonstrating mutability and immutability
my_list = [1, 2, 3]
my_list[0] = 10  # Modifying the list
print(f"Modified list: {my_list}")

my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # Uncommenting this will raise a TypeError
