
# List Assignment
[a, b] = [1, 2]
print("List Assignment:")
print(f"a = {a}, b = {b}")  # Output: a = 1, b = 2

# Tuple Assignment
a, b = (3, 4)
print("\nTuple Assignment:")
print(f"a = {a}, b = {b}")  # Output: a = 3, b = 4

# Modifying a list
my_list = [1, 2, 3]
my_list[0] = 10
print("\nModified List:")
print(my_list)  # Output: [10, 2, 3]

# Trying to modify a tuple (will raise an error)
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # Uncommenting this line will raise a TypeError
